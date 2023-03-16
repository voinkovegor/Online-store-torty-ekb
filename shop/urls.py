from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('contacts/', views.contacts,
         name='contacts'),
    path('toppings_and_decoration/', views.toppings_and_decoration,
         name='toppings_and_decoration'),
    path('tiered_cakes/', views.tiered_cakes,
         name='tiered_cakes'),
    path('order_and_payment/', views.order_and_payment,
         name='order_and_payment'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]