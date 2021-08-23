from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=255, blank=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Item(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):

    user = models.CharField(max_length=255)
    items = models.CharField(max_length=1000, blank=False)
    name = models.CharField(max_length=255, blank=False)
    surname = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    address = models.CharField(max_length=1000, blank=False)
    city = models.CharField(max_length=255, blank=False)
    date = models.DateTimeField(auto_now_add=True)
