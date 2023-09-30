from . import views
from django.urls import path

urlpatterns = [
    path('',views.allproducts, name='allproducts'),
    path('Cart/', views.cart, name='cart'),
    path('<slug:slug_c>/', views.allproducts, name='product_by_category'),
    path('<slug:slug_c>/<slug_p>/', views.prod_det, name='product_catdetail'),




]
