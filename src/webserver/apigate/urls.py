from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('prod/<str:name>/', views.handle_product_api, name="get_product")
]