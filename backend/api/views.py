from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Property, ContactRequest

def get_properties(request):
    properties = Property.objects.all()
    
    # Filtering
    search = request.GET.get('search', '')
    prop_type = request.GET.get('type', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')

    if search:
        properties = properties.filter(Q(title__icontains=search) | Q(city__icontains=search) | Q(state__icontains=search))
    if prop_type:
        properties = properties.filter(property_type=prop_type)
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)

    # Build response data with full image URL
    data = []
    for prop in properties:
        image_url = ''
        if prop.image:
            image_url = request.build_absolute_uri(prop.image.url)
            
        data.append({
            'id': prop.id,
            'title': prop.title,
            'description': prop.description,
            'property_type': prop.property_type,
            'price': str(prop.price),
            'address': prop.address,
            'city': prop.city,
            'state': prop.state,
            'location': f"{prop.city}, {prop.state}",
            'bedrooms': prop.bedrooms,
            'bathrooms': prop.bathrooms,
            'area_sqft': prop.area_sqft,
            'image_url': image_url,
            'is_available': prop.is_available,
        })
        
    return JsonResponse(data, safe=False)


@csrf_exempt
def contact_request(request):
    if request.method == 'POST':
        import re
        data = json.loads(request.body)
        
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        company = data.get('company', '').strip()
        message = data.get('message', '').strip()

        # Check if fields are empty
        if not name or not email or not message:
            return JsonResponse({'error': 'Name, email, and message are required.'}, status=400)

        # Validate name (Only letters, spaces, hyphens, apostrophes)
        if not re.match(r"^[a-zA-Z\s\-\']+$", name):
            return JsonResponse({'error': 'Name should only contain letters and spaces.'}, status=400)

        # Validate email (Strict format checking)
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            return JsonResponse({'error': 'Please enter a valid email address (e.g., example@domain.com).'}, status=400)

        contact = ContactRequest.objects.create(
            name=name,
            email=email,
            company=company,
            message=message
        )

        return JsonResponse({
            'message': 'Contact request submitted successfully'
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)
