from typing import List
from django.shortcuts import render
from .models import Order
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin 

    

class OrdersView(ListView):
    model = Order
    template_name = "orders/orders_view.html"

    def get(self, request, *args, **kwargs):
        self.object = Order.objects.all()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object
        return context

    def get_queryset(self):
        return self.object

