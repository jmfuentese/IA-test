from typing import List
from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin 

    
class CreateProduct(SuccessMessageMixin, CreateView):
    model = Product
    form = ProductForm
    fields = "__all__"
    template_name = "products/product_create.html"
    success_message = "Product created successfully!"

    def get_success_url(self):
        return reverse("productsList")

class ProductsList(ListView):
    model = Product
    template_name = "products/product_list.html"

    def get(self, request, *args, **kwargs):
        self.object = Product.objects.all()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object
        return context

    def get_queryset(self):
        return self.object


class ProductDetail(DetailView):
    model = Product



class ProductUpdate(SuccessMessageMixin, UpdateView):
    model = Product
    form = ProductForm
    fields = "__all__"
    success_message = "Product updated successfully!"

    def get_success_url(self):
        return reverse("productsList")


class ProductDelete(SuccessMessageMixin, DeleteView):
    model = Product
    
    success_url = reverse_lazy('productsList')