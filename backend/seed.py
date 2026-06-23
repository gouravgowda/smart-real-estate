import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from api.models import Property, User
from django.core.files.base import ContentFile
import urllib.request
import json

def seed_db():
    print("Clearing database...")
    Property.objects.all().delete()
    User.objects.all().delete()

    print("Creating owner...")
    owner = User.objects.create(full_name='Rohan Sharma', email='rohan@demo.com', password='password123', phone='9876543210', role='owner')

    properties_data = [
        # Original 6 Indian Properties
        {
            'title': 'Luxury Villa in Bandra West',
            'description': 'A beautiful luxury villa with a private pool and sea view. Perfect for a family seeking comfort and elegance in Mumbai.',
            'property_type': 'villa',
            'price': '45000000.00',
            'address': '123 Carter Road, Bandra West',
            'city': 'Mumbai',
            'state': 'MH',
            'bedrooms': 5,
            'bathrooms': 6,
            'area_sqft': 6000,
            'image_url': 'https://images.unsplash.com/photo-1613977257363-707ba9348227?w=800&q=80'
        },
        {
            'title': 'Modern Apartment in Indiranagar',
            'description': 'Sleek, modern apartment located in the heart of the IT hub with breathtaking city views and premium amenities.',
            'property_type': 'apartment',
            'price': '15000000.00',
            'address': '456 100ft Road Apt 402',
            'city': 'Bangalore',
            'state': 'KA',
            'bedrooms': 2,
            'bathrooms': 2,
            'area_sqft': 1200,
            'image_url': 'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800&q=80'
        },
        {
            'title': 'Cozy House in Salt Lake',
            'description': 'A charming home in a quiet neighborhood, featuring a large backyard and newly renovated kitchen.',
            'property_type': 'house',
            'price': '8500000.00',
            'address': '789 Sector V',
            'city': 'Kolkata',
            'state': 'WB',
            'bedrooms': 3,
            'bathrooms': 2,
            'area_sqft': 1800,
            'image_url': 'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=800&q=80'
        },
        {
            'title': 'Commercial Office Space in Cyber City',
            'description': 'Spacious and bright commercial space ideal for a tech startup or creative agency.',
            'property_type': 'commercial',
            'price': '120000000.00',
            'address': '101 DLF Cyber City',
            'city': 'Gurugram',
            'state': 'HR',
            'bedrooms': 0,
            'bathrooms': 4,
            'area_sqft': 4500,
            'image_url': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&q=80'
        },
        {
            'title': 'Beachfront Paradise Villa in Candolim',
            'description': 'Wake up to the sound of waves in this stunning beachfront property with direct ocean access.',
            'property_type': 'villa',
            'price': '65000000.00',
            'address': '55 Beach Road, Candolim',
            'city': 'Goa',
            'state': 'GA',
            'bedrooms': 4,
            'bathrooms': 4,
            'area_sqft': 3500,
            'image_url': 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800&q=80'
        },
        {
            'title': 'Rustic Mountain Cottage in Manali',
            'description': 'A peaceful retreat nestled in the mountains. Features a stone fireplace and wrap-around deck.',
            'property_type': 'house',
            'price': '35000000.00',
            'address': '22 Mall Road',
            'city': 'Manali',
            'state': 'HP',
            'bedrooms': 3,
            'bathrooms': 2,
            'area_sqft': 2100,
            'image_url': 'https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=800&q=80'
        },
        # 30 New Properties
        {
            'title': 'Premium Flat in Banjara Hills',
            'description': 'An ultra-premium flat in one of Hyderabad\'s most affluent neighborhoods, featuring imported marble and smart home automation.',
            'property_type': 'apartment',
            'price': '25000000.00',
            'address': 'Road No. 12, Banjara Hills',
            'city': 'Hyderabad',
            'state': 'TG',
            'bedrooms': 4,
            'bathrooms': 4,
            'area_sqft': 3200,
            'image_url': 'https://images.unsplash.com/photo-1502672260266-1c1c24240f38?w=800&q=80'
        },
        {
            'title': 'Heritage House in Pink City',
            'description': 'A beautifully restored traditional house in Jaipur with intricate frescoes and a central courtyard.',
            'property_type': 'house',
            'price': '18000000.00',
            'address': 'Bapu Bazaar, Civil Lines',
            'city': 'Jaipur',
            'state': 'RJ',
            'bedrooms': 4,
            'bathrooms': 3,
            'area_sqft': 2800,
            'image_url': 'https://images.unsplash.com/photo-1449844908441-8829872d2607?w=800&q=80'
        },
        {
            'title': 'Sea-Facing Penthouse in Marine Drive',
            'description': 'An iconic sea-facing penthouse offering unparalleled views of the Queen\'s Necklace.',
            'property_type': 'apartment',
            'price': '85000000.00',
            'address': 'Netaji Subhash Chandra Bose Road',
            'city': 'Mumbai',
            'state': 'MH',
            'bedrooms': 4,
            'bathrooms': 5,
            'area_sqft': 4000,
            'image_url': 'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=800&q=80'
        },
        {
            'title': 'Tech Park Office in Hitec City',
            'description': 'A modern, fully furnished office space in the heart of Hyderabad\'s IT corridor.',
            'property_type': 'commercial',
            'price': '45000000.00',
            'address': 'Mindspace IT Park, Madhapur',
            'city': 'Hyderabad',
            'state': 'TG',
            'bedrooms': 0,
            'bathrooms': 2,
            'area_sqft': 2500,
            'image_url': 'https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=800&q=80'
        },
        {
            'title': 'Independent Villa in Koregaon Park',
            'description': 'A spacious luxury villa with lush green surroundings in Pune\'s most desirable locality.',
            'property_type': 'villa',
            'price': '32000000.00',
            'address': 'North Main Road, Koregaon Park',
            'city': 'Pune',
            'state': 'MH',
            'bedrooms': 4,
            'bathrooms': 4,
            'area_sqft': 3500,
            'image_url': 'https://images.unsplash.com/photo-1580587771525-78b9dba3b914?w=800&q=80'
        },
        {
            'title': 'Studio Apartment in Viman Nagar',
            'description': 'A trendy and compact studio apartment ideal for students and IT professionals.',
            'property_type': 'apartment',
            'price': '4500000.00',
            'address': 'Symbiosis Road, Viman Nagar',
            'city': 'Pune',
            'state': 'MH',
            'bedrooms': 1,
            'bathrooms': 1,
            'area_sqft': 600,
            'image_url': 'https://images.unsplash.com/photo-1536376072261-38c75010e6c9?w=800&q=80'
        },
        {
            'title': 'Grand Mansion in Vasant Vihar',
            'description': 'A sprawling mansion featuring state-of-the-art security, servant quarters, and an expansive garden.',
            'property_type': 'villa',
            'price': '150000000.00',
            'address': 'Vasant Vihar',
            'city': 'New Delhi',
            'state': 'DL',
            'bedrooms': 6,
            'bathrooms': 7,
            'area_sqft': 10000,
            'image_url': 'https://images.unsplash.com/photo-1512915922686-57c11dde9b6b?w=800&q=80'
        },
        {
            'title': 'Lake View Apartment in Powai',
            'description': 'Overlooking the Powai lake, this beautiful apartment offers serenity within the bustling city of Mumbai.',
            'property_type': 'apartment',
            'price': '22000000.00',
            'address': 'Hiranandani Gardens, Powai',
            'city': 'Mumbai',
            'state': 'MH',
            'bedrooms': 3,
            'bathrooms': 3,
            'area_sqft': 1500,
            'image_url': 'https://images.unsplash.com/photo-1484154218962-a197022b5858?w=800&q=80'
        },
        {
            'title': 'Retail Shop in Connaught Place',
            'description': 'Prime commercial retail space located in one of Delhi\'s most iconic commercial hubs.',
            'property_type': 'commercial',
            'price': '85000000.00',
            'address': 'Inner Circle, Connaught Place',
            'city': 'New Delhi',
            'state': 'DL',
            'bedrooms': 0,
            'bathrooms': 1,
            'area_sqft': 800,
            'image_url': 'https://images.unsplash.com/photo-1555529771-835f59fc5efe?w=800&q=80'
        },
        {
            'title': 'Luxury Condo in Whitefield',
            'description': 'Modern condominium complex with club house, gym, and swimming pool in Bangalore\'s IT hub.',
            'property_type': 'apartment',
            'price': '11000000.00',
            'address': 'ITPB Main Road, Whitefield',
            'city': 'Bangalore',
            'state': 'KA',
            'bedrooms': 2,
            'bathrooms': 2,
            'area_sqft': 1150,
            'image_url': 'https://images.unsplash.com/photo-1502672023488-70e25813eb80?w=800&q=80'
        },
        {
            'title': 'Spacious House in Anna Nagar',
            'description': 'A massive independent house located in a peaceful residential street in Chennai.',
            'property_type': 'house',
            'price': '45000000.00',
            'address': '2nd Avenue, Anna Nagar',
            'city': 'Chennai',
            'state': 'TN',
            'bedrooms': 4,
            'bathrooms': 4,
            'area_sqft': 3600,
            'image_url': 'https://images.unsplash.com/photo-1510798831971-661eb04b3739?w=800&q=80'
        },
        {
            'title': 'Duplex Apartment in Alwarpet',
            'description': 'An elegant duplex apartment with a private terrace garden in a premium Chennai neighborhood.',
            'property_type': 'apartment',
            'price': '38000000.00',
            'address': 'TTK Road, Alwarpet',
            'city': 'Chennai',
            'state': 'TN',
            'bedrooms': 3,
            'bathrooms': 4,
            'area_sqft': 2400,
            'image_url': 'https://images.unsplash.com/photo-1515263487990-61b07816b324?w=800&q=80'
        },
        {
            'title': 'Farmhouse in Chhatarpur',
            'description': 'A sprawling farmhouse perfect for weekend getaways, featuring a large swimming pool and landscaped gardens.',
            'property_type': 'villa',
            'price': '95000000.00',
            'address': 'Chhatarpur Farms',
            'city': 'New Delhi',
            'state': 'DL',
            'bedrooms': 5,
            'bathrooms': 6,
            'area_sqft': 8500,
            'image_url': 'https://images.unsplash.com/photo-1588880331179-bc9b93a8cb65?w=800&q=80'
        },
        {
            'title': 'Co-working Space in Koramangala',
            'description': 'Ready-to-move-in co-working space spanning two floors in the startup capital of India.',
            'property_type': 'commercial',
            'price': '65000000.00',
            'address': '80 Feet Road, Koramangala',
            'city': 'Bangalore',
            'state': 'KA',
            'bedrooms': 0,
            'bathrooms': 6,
            'area_sqft': 5000,
            'image_url': 'https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=800&q=80'
        },
        {
            'title': 'Bungalow in Jubilee Hills',
            'description': 'An architectural marvel located in Hyderabad\'s most exclusive neighborhood, featuring a home theater and gym.',
            'property_type': 'villa',
            'price': '180000000.00',
            'address': 'Road No. 36, Jubilee Hills',
            'city': 'Hyderabad',
            'state': 'TG',
            'bedrooms': 6,
            'bathrooms': 7,
            'area_sqft': 9000,
            'image_url': 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&q=80'
        },
        {
            'title': 'Budget Flat in New Town',
            'description': 'An affordable, well-ventilated apartment in a rapidly developing township.',
            'property_type': 'apartment',
            'price': '3500000.00',
            'address': 'Action Area I, New Town',
            'city': 'Kolkata',
            'state': 'WB',
            'bedrooms': 2,
            'bathrooms': 1,
            'area_sqft': 850,
            'image_url': 'https://images.unsplash.com/photo-1554995207-c18c203602cb?w=800&q=80'
        },
        {
            'title': 'Riverside Home in SG Highway',
            'description': 'A beautiful standalone home near the Sabarmati riverfront with excellent connectivity.',
            'property_type': 'house',
            'price': '16000000.00',
            'address': 'SG Highway',
            'city': 'Ahmedabad',
            'state': 'GJ',
            'bedrooms': 3,
            'bathrooms': 3,
            'area_sqft': 2200,
            'image_url': 'https://images.unsplash.com/photo-1576941089067-2de3c901e126?w=800&q=80'
        },
        {
            'title': 'Luxury Apartment in Bodakdev',
            'description': 'A high-rise luxury apartment with panoramic views of Ahmedabad city.',
            'property_type': 'apartment',
            'price': '28000000.00',
            'address': 'Sindhu Bhavan Road, Bodakdev',
            'city': 'Ahmedabad',
            'state': 'GJ',
            'bedrooms': 4,
            'bathrooms': 4,
            'area_sqft': 2800,
            'image_url': 'https://images.unsplash.com/photo-1542314831-c6a4d14ab1c8?w=800&q=80'
        },
        {
            'title': 'IT Park Space in Hinjewadi',
            'description': 'Large commercial floor plate available in Pune\'s biggest IT zone.',
            'property_type': 'commercial',
            'price': '95000000.00',
            'address': 'Phase 1, Hinjewadi Rajiv Gandhi Infotech Park',
            'city': 'Pune',
            'state': 'MH',
            'bedrooms': 0,
            'bathrooms': 8,
            'area_sqft': 12000,
            'image_url': 'https://images.unsplash.com/photo-1497366811353-6870744d04b2?w=800&q=80'
        },
        {
            'title': 'Colonial House in Fort Kochi',
            'description': 'A historic colonial-era house with antique wooden flooring and Portuguese architecture.',
            'property_type': 'house',
            'price': '35000000.00',
            'address': 'Princess Street, Fort Kochi',
            'city': 'Kochi',
            'state': 'KL',
            'bedrooms': 4,
            'bathrooms': 3,
            'area_sqft': 3100,
            'image_url': 'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=800&q=80'
        },
        {
            'title': 'Waterfront Villa in Marine Drive',
            'description': 'An exquisite villa overlooking the backwaters of Kochi.',
            'property_type': 'villa',
            'price': '42000000.00',
            'address': 'Marine Drive',
            'city': 'Kochi',
            'state': 'KL',
            'bedrooms': 4,
            'bathrooms': 5,
            'area_sqft': 3800,
            'image_url': 'https://images.unsplash.com/photo-1510080470650-653a9482f3fb?w=800&q=80'
        },
        {
            'title': 'Elegant Apartment in Gomti Nagar',
            'description': 'A newly built, elegant apartment in Lucknow\'s most planned residential area.',
            'property_type': 'apartment',
            'price': '9500000.00',
            'address': 'Vibhuti Khand, Gomti Nagar',
            'city': 'Lucknow',
            'state': 'UP',
            'bedrooms': 3,
            'bathrooms': 2,
            'area_sqft': 1600,
            'image_url': 'https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?w=800&q=80'
        },
        {
            'title': 'Sprawling Estate in Civil Lines',
            'description': 'A traditional large estate offering immense privacy and classic charm.',
            'property_type': 'house',
            'price': '55000000.00',
            'address': 'Civil Lines',
            'city': 'Prayagraj',
            'state': 'UP',
            'bedrooms': 5,
            'bathrooms': 4,
            'area_sqft': 5500,
            'image_url': 'https://images.unsplash.com/photo-1464146072230-91cabc968266?w=800&q=80'
        },
        {
            'title': 'Showroom Space in Hazratganj',
            'description': 'A high-visibility showroom space located in the bustling shopping district of Lucknow.',
            'property_type': 'commercial',
            'price': '75000000.00',
            'address': 'Hazratganj Main Road',
            'city': 'Lucknow',
            'state': 'UP',
            'bedrooms': 0,
            'bathrooms': 2,
            'area_sqft': 3000,
            'image_url': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=800&q=80'
        },
        {
            'title': 'Modern Villa in Pal Bhawan',
            'description': 'A smart-home enabled modern villa with a sleek facade and contemporary interiors.',
            'property_type': 'villa',
            'price': '28000000.00',
            'address': 'Pal Road',
            'city': 'Jodhpur',
            'state': 'RJ',
            'bedrooms': 4,
            'bathrooms': 4,
            'area_sqft': 3000,
            'image_url': 'https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=800&q=80'
        },
        {
            'title': 'Valley View Apartment in Dehradun',
            'description': 'A serene apartment offering uninterrupted views of the Doon Valley and the Himalayas.',
            'property_type': 'apartment',
            'price': '12000000.00',
            'address': 'Rajpur Road',
            'city': 'Dehradun',
            'state': 'UK',
            'bedrooms': 3,
            'bathrooms': 3,
            'area_sqft': 1750,
            'image_url': 'https://images.unsplash.com/photo-1513694203232-719a280e022f?w=800&q=80'
        },
        {
            'title': 'Hillside Cottage in Mussoorie',
            'description': 'A quaint hillside cottage perfect for a summer retreat, featuring wooden interiors and a fireplace.',
            'property_type': 'house',
            'price': '18000000.00',
            'address': 'Camel\'s Back Road',
            'city': 'Mussoorie',
            'state': 'UK',
            'bedrooms': 2,
            'bathrooms': 2,
            'area_sqft': 1400,
            'image_url': 'https://images.unsplash.com/photo-1449158743715-0a90ebb6d2d8?w=800&q=80'
        },
        {
            'title': 'Premium Commercial Tower in OMR',
            'description': 'A premium commercial office space in Chennai\'s IT corridor.',
            'property_type': 'commercial',
            'price': '250000000.00',
            'address': 'Old Mahabalipuram Road',
            'city': 'Chennai',
            'state': 'TN',
            'bedrooms': 0,
            'bathrooms': 10,
            'area_sqft': 25000,
            'image_url': 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&q=80'
        },
        {
            'title': 'Luxury Condominium in Sector 50',
            'description': 'A beautiful condominium with all modern amenities in a highly sought-after sector in Noida.',
            'property_type': 'apartment',
            'price': '16500000.00',
            'address': 'Sector 50',
            'city': 'Noida',
            'state': 'UP',
            'bedrooms': 3,
            'bathrooms': 3,
            'area_sqft': 1950,
            'image_url': 'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=800&q=80'
        },
        {
            'title': 'Palatial House in Sadashivanagar',
            'description': 'A magnificent house in one of Bangalore\'s oldest and most prestigious neighborhoods.',
            'property_type': 'house',
            'price': '85000000.00',
            'address': 'Sadashivanagar Main',
            'city': 'Bangalore',
            'state': 'KA',
            'bedrooms': 5,
            'bathrooms': 5,
            'area_sqft': 5200,
            'image_url': 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800&q=80'
        },
        {
            'title': 'Sea-View Apartment in Besant Nagar',
            'description': 'A breezy sea-view apartment steps away from Elliot\'s Beach.',
            'property_type': 'apartment',
            'price': '26000000.00',
            'address': 'Besant Nagar',
            'city': 'Chennai',
            'state': 'TN',
            'bedrooms': 3,
            'bathrooms': 3,
            'area_sqft': 1800,
            'image_url': 'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800&q=80'
        },
        {
            'title': 'Industrial Warehouse in Peenya',
            'description': 'A massive industrial warehouse space located in one of Asia\'s largest industrial areas.',
            'property_type': 'commercial',
            'price': '55000000.00',
            'address': 'Peenya Industrial Area',
            'city': 'Bangalore',
            'state': 'KA',
            'bedrooms': 0,
            'bathrooms': 2,
            'area_sqft': 15000,
            'image_url': 'https://images.unsplash.com/photo-1586528116311-ad8ed7c66363?w=800&q=80'
        },
        {
            'title': 'Elegant Villa in ECR',
            'description': 'An elegant, resort-style villa located on the scenic East Coast Road.',
            'property_type': 'villa',
            'price': '65000000.00',
            'address': 'East Coast Road',
            'city': 'Chennai',
            'state': 'TN',
            'bedrooms': 4,
            'bathrooms': 5,
            'area_sqft': 4200,
            'image_url': 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&q=80'
        },
        {
            'title': 'Posh Apartment in Golf Course Road',
            'description': 'A luxury apartment situated on the prestigious Golf Course Road in Gurugram.',
            'property_type': 'apartment',
            'price': '45000000.00',
            'address': 'DLF Phase 5, Golf Course Road',
            'city': 'Gurugram',
            'state': 'HR',
            'bedrooms': 4,
            'bathrooms': 4,
            'area_sqft': 3500,
            'image_url': 'https://images.unsplash.com/photo-1502672260266-1c1c24240f38?w=800&q=80'
        },
        {
            'title': 'Boutique Hotel Property in Udaipur',
            'description': 'A commercial property currently operating as a boutique heritage hotel near Lake Pichola.',
            'property_type': 'commercial',
            'price': '120000000.00',
            'address': 'Chandpole, Near Lake Pichola',
            'city': 'Udaipur',
            'state': 'RJ',
            'bedrooms': 12,
            'bathrooms': 12,
            'area_sqft': 8000,
            'image_url': 'https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800&q=80'
        },
        {
            'title': 'Contemporary House in Jayanagar',
            'description': 'A contemporary designed independent house located in a quiet block of Jayanagar.',
            'property_type': 'house',
            'price': '38000000.00',
            'address': '4th Block, Jayanagar',
            'city': 'Bangalore',
            'state': 'KA',
            'bedrooms': 4,
            'bathrooms': 3,
            'area_sqft': 2600,
            'image_url': 'https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=800&q=80'
        }
    ]

    for p in properties_data:
        print(f"Creating property: {p['title']}...")
        prop = Property(
            owner=owner,
            title=p['title'],
            description=p['description'],
            property_type=p['property_type'],
            price=p['price'],
            address=p['address'],
            city=p['city'],
            state=p['state'],
            bedrooms=p.get('bedrooms', 0),
            bathrooms=p.get('bathrooms', 0),
            area_sqft=p.get('area_sqft', 0),
        )
        
        try:
            req = urllib.request.Request(p['image_url'], headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req)
            # Create a safe filename
            safe_title = ''.join(c for c in p['title'] if c.isalnum() or c == ' ').strip().replace(' ', '_').lower()
            image_name = safe_title + '.jpg'
            prop.image.save(image_name, ContentFile(response.read()), save=False)
        except Exception as e:
            print(f"  -> Failed to download image: {e}")
            
        prop.save()

    print("Database seeded successfully!")

if __name__ == '__main__':
    seed_db()
