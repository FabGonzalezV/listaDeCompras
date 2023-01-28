from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from . import models

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
    return render(request, 'carrito/base.html')