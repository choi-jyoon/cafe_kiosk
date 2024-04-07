from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from django.urls import reverse, reverse_lazy
from django.http import Http404, HttpResponse
from cafe.models import Category, Menu, Order
# Create your views here.

class CategoryLV(ListView):
    model = Category

class CategoryDV(DetailView):
    model = Category
    
class MenuLV(ListView):
    model = Menu
    
    def get_queryset(self):
        category_pk = self.kwargs.get('pk')
        
        queryset = Menu.objects.filter(category__id = category_pk)
        
        return queryset
    
class MenuDV(DetailView):
    model = Menu
    
    def get_object(self, queryset=None):
        category_pk = self.kwargs.get('pk')
        menu_pk = self.kwargs.get('pk2')
        
        try:
            queryset = Menu.objects.get(category__id=category_pk, id=menu_pk)
        except Menu.DoesNotExist:
            raise Http404("Menu does not exist")
        
        return queryset
    
class ManageView(TemplateView):
    template_name = 'cafe/manage.html'
    
class MenuCV(CreateView):
    model = Menu
    fields = ['name', 'price', 'category']
    success_url = reverse_lazy('cafe:index')
    
class CategoryCV(CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('cafe:index')
    
class OrderView(TemplateView):
    template_name = 'cafe/order.html'

    def post(self, request, category_id, menu_id):
        quantity = request.POST.get('quantity')
        ice = request.POST.get('ice')
        menu = Menu.objects.get(pk=menu_id)
        price = menu.price
        order = Order.objects.create(menu=menu, quantity=quantity, ice=ice, price = int(price)*int(quantity))
        return render(request, self.template_name, {'order': order})

class PayView(UpdateView):
    model = Order
    fields=['pay']
    template_name = 'cafe/pay.html'
    def get_success_url(self):
        return reverse_lazy('cafe:pay_success')
    
class PaySuccessView(TemplateView):
    template_name = "cafe/pay_success.html"
    