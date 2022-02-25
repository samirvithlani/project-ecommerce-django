from os import name
from django.urls import path
from .views import *
from generic.views import *

app_name = 'product_urls'

urlpatterns = [
    path('product_creation/', BaseCreateView.as_view(), name='product_creation'),
    path('update/<int:pk>', BaseUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BaseDeleteView.as_view(), name='delete'),

    path('brand/', BrandCreateView.as_view(), name='brand'),
    path('update_brand/<int:pk>', UpdateBrandView.as_view(), name='update_brand'),
    path('delete_brand/<int:pk>', DeleteBrandView.as_view(), name='delete_brand'), 

    path('category/', CategoryCreateView.as_view(), name='category'),
    path('update_category/<int:pk>', UpdateCategoryView.as_view(), name='update_category'),
    path('delete_category/<int:pk>', DeleteCategoryView.as_view(), name='delete_category'),

    path('products/', CategoryBrandFilterView.as_view(), name='categories'), 
    path('single_product/<pk>', SingleProductView.as_view(),name='single_product'),
    path('search/', SearchView.as_view(), name='search'),

    
]
