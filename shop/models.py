from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('smartphone', 'Smartphone'),
        ('laptop', 'Laptop'),
        ('tablet', 'Tablet'),
        ('wearable', 'Wearable'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='products/')
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        return f'Review for {self.product.name}'
