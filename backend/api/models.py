from django.db import models


class User(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('owner', 'Owner'),
        ('customer', 'Customer'),
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Property(models.Model):
    PROPERTY_TYPES = (
        ('apartment', 'Apartment'),
        ('villa', 'Villa'),
        ('house', 'House'),
        ('commercial', 'Commercial'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area_sqft = models.IntegerField()
    image = models.ImageField(upload_to='properties/')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    booking_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.full_name} - {self.property.title}"


class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
