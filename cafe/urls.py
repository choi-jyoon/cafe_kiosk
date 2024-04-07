from django.urls import path

from . import views

app_name = "cafe"

urlpatterns = [
    path("", views.CategoryLV.as_view(), name="index"),      # 제네릭 뷰 사용
    path("<int:pk>/", views.MenuLV.as_view(), name="detail"),
    path("<int:pk>/<int:pk2>", views.MenuDV.as_view(), name="menudetail"),
    path('create/', views.CategoryCV.as_view(), name='category_create'),
    path('menu/create/', views.MenuCV.as_view(), name='menu_create'),
    path('<int:category_id>/<int:menu_id>/order/', views.OrderView.as_view(), name='order'),
    path('manage/', views.ManageView.as_view(), name='manage'),
    path('<int:pk>/order/', views.PayView.as_view(), name='pay'),
    path('order/pay', views.PaySuccessView.as_view(), name='pay_success'),
]