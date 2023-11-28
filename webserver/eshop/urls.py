from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('product/<str:name>/', views.product, name='product'),
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
    path('cart/', views.cart, name='cart'),
    path('order/', views.order, name='order'),
]