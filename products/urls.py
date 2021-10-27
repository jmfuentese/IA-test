from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.CreateProduct.as_view(), name='createProduct'),
    path('list/', views.ProductsList.as_view(), name='productsList'),
    path('detail/<int:pk>', views.ProductDetail.as_view(template_name="products/detail.html"), name="detailView"),
    path('update/<int:pk>', views.ProductUpdate.as_view(template_name="products/product_update.html"), name="updateView"),
    path('delete/<int:pk>', views.ProductDelete.as_view(), name="deleteView"),
    
]

