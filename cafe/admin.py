from django.contrib import admin
from cafe.models import Category, Menu, Order
# Register your models here.

@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display=('id', 'name')
    
@admin.register(Menu)
class PostAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'price', 'category')
    
@admin.register(Order)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu', 'quantity', 'ice', 'price')