from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('prod/<str:name>/', views.get_product, name="get_product")
]