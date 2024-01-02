from django.urls import path
from . import views

urlpatterns = [
    path('',                    views.home, name='home'),
    path('search/',             views.search, name='search'),
    path('product/<str:name>/', views.product, name='product'),
    path('login/',              views.login, name='login'),
    path('account/',            views.account, name='account'),
    path('cart/',               views.cart, name='cart'),
    path('order/',              views.order, name='order'),

    path('admin/',              views.admin_home, name='admin-home'),
    path('admin/orders/',       views.admin_orders, name='admin-orders'),
    path('admin/products/',     views.admin_products, name='admin-products'),
    path('admin/reviews/',      views.admin_reviews, name='admin-reviews'),
    path('admin/users/',        views.admin_users, name='admin-users'),

    path('superuser/',          views.superuser_home, name='superuser-home')
]