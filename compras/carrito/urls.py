from django.urls import path
from .views import products, registrarProducto, eliminarProducto, editarProducto, edicionProducto


urlpatterns = [
    path('', products, name='products'),
    path('registrarProducto/', registrarProducto, name='register-product'),
    path('edicionProducto/editarProducto/', editarProducto, name='upd-product'),
    path('edicionProducto/<id>', edicionProducto, name='update-product'),
    path('eliminarProducto/<product>', eliminarProducto, name='delete-product'),
]