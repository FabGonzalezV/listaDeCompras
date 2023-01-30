from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib import messages
from . import models
from .models import ListProducts

class ProductsListView(ListView): 
    model = models.ListProducts

class ProductsListDetailView(DetailView):  
    model = models.ListProducts

class ProductsListUpdateView(UpdateView):  
    model = models.ListProducts
    fields = "__all__" 

class ProductsListDeleteView(DeleteView): 
    model = models.ListProducts
    success_url = '/products-list/'

class ProductsListCreateView(CreateView):  
    model = models.ListProducts
    fields = "__all__"     

@login_required
def products(request):
    products = ListProducts.objects.filter(client=request.user, status_delete=False)
    messages.success(request, '¡Productos listados!')
    return render(request, 'carrito/gestionProductos.html', {"productos": products})

def registrarProducto(request):
    product = request.POST['producto']
    type = request.POST['categoria']
    client = request.user
    producto = ListProducts.objects.create(product=product, type=type, client=client)
    messages.success(request, '¡Producto registrado!')
    return redirect('products')

def edicionProducto(request, id):
    producto = ListProducts.objects.get(id=id)
    return render(request, 'carrito/edicionProducto.html',  {"producto": producto})

def editarProducto(request):
    id = request.POST['idproducto']
    product = request.POST['producto']
    type = request.POST['categoria']
    producto = ListProducts.objects.get(id=id)
    producto.product = product
    producto.type = type
    producto.save()
    messages.success(request, '¡Producto actualizado!')
    return redirect('products')

def eliminarProducto(request, id):
    producto = ListProducts.objects.get(id=id)
    producto.status_delete = True
    producto.save()
    messages.success(request, '¡Producto eliminado!')
    return redirect('products')

