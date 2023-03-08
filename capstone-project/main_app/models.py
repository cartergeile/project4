from django.db import models

# Create your models here.

CATEGORY_CHOICES=(
    ('D', 'Driver'),
    ('I', 'Irons'),
    ('W', 'Wedge'),
    ('P', 'Putter'),
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(max_length=450)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.name