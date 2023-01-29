from django.urls import path
from .views import home, exit
from carrito.views import products, registrarProducto


urlpatterns = [
    path('', home, name='home'),
    # path('products/', products, name='products'),
    # path('registrarProducto/', registrarProducto, name='register-product'),
    path('logout/', exit, name='exit'),
]