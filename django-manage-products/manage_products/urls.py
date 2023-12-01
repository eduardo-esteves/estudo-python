from django.urls import path

from manage_products import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('product', views.product, name='product'),
]
