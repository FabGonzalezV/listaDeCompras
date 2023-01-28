from django.urls import path
from .views import home, exit
from carrito.views import products


urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('logout/', exit, name='exit'),
]