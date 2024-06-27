from django.db import models

class Phone(models.Model):
    LOCATION_CHOICES = [
        ('Ottapalam', 'Ottapalam'),
        ('Cherupulasseri', 'Cherupulasseri'),
        ('Perintalmanna', 'Perintalmanna'),
    ]
    COLOUR_CHOICES = [
        ('Black','Black'),
        ('Blue','Blue'),
        ('Green','Green'),
        ('Yellow','Yellow'),
        ('Black Titanium', 'Black Titanium'),
        ('Blue Titanium', 'Blue Titanium'),
        ('White Titanium', 'White Titanium'),
        ('Natural Titanium', 'Natural Titanium'),
        ('Midnight','Midnight'),
        ('Starlight', 'Starlight'),
        ('Purple', 'Purple'),
        ('Red', 'Red'),
        ('Space Black', 'Space Black'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Deep Purple', 'Deep Purple'),
        ('Pink', 'Pink'),
        ('Graphite', 'Graphite'),
        ('Sierra Blue', 'Sierra Blue'),
        ('Alpine Green', 'Alpine Green'),
    ]
    Storage_Capacity_Choices=[
        ('64 GB','64 GB'),
        ('128 GB', '128 GB'),
        ('256 GB', '256 GB'),
        ('512 GB', '512 GB'),
        ('1 TB', '1 TB'),
    ]

    name = models.CharField(max_length=100)
    year = models.IntegerField()
    battery_health = models.IntegerField()
    colour=models.CharField(max_length=50,choices=COLOUR_CHOICES)
    images = models.ImageField(upload_to='phone_images/')
    storage_capacity=models.CharField(max_length=50,choices=Storage_Capacity_Choices)
    description = models.TextField()
    quantity = models.IntegerField()
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)

    def __str__(self):
        return self.name
