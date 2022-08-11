from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    ingredients = models.ManyToManyField(Ingredient, blank=False)
    description = models.CharField(max_length=250)
    quantity = models.IntegerField(default=0)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    date = datetime.today().strftime('%d-%m-%Y')
    order_by = models.CharField(max_length=50)
    dishes_ordered = models.ManyToManyField(Dish, blank=False)
    order_date = models.DateField(
        auto_now_add=False, editable=True, default=date)

    def __str__(self):
        return str(self.order_by)
