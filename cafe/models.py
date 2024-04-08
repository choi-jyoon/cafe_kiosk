from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='CATEGORY NAME', max_length=200)
    
    def __str__(self):
        return self.name


class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='MENU NAME', max_length=50, unique=True)
    price = models.IntegerField(verbose_name='PRICE', default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name="PRICE", default=0)
    quantity = models.IntegerField(verbose_name="QUANTITY", default=0)
    ice = models.BooleanField(verbose_name='ICE', default=True)
    pay = models.BooleanField(verbose_name='PAY', default=False)
    