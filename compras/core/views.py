from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from carrito.models import ListProducts

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

# @login_required
# def products(request):
#     return render(request, 'compras/carrito/templates/base.html')
# def registrarProducto(request):
#     print(request)
#     product = request.POST['Producto']
#     type = request.POST['categoria']
#     client = request.user
#     # try:
#     producto = ListProducts.objects.create(product=product, type=type, client=client)
#     # except:
#     #     print('No se guardo')
#     return redirect('http://127.0.0.1:8000/products/')
def exit(request):
    logout(request)
    return redirect('home')