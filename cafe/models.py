from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200)


class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
