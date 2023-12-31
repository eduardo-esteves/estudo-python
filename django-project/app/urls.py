from django.urls import path

from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('products', views.products, name='products'),
    path('product/<int:id>', views.product, name='product'),
]
