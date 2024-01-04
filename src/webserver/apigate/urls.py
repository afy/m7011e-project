from django.urls import path
from . import views

urlpatterns = [
    path('prod/<int:id>/', views.handle_product_crud, name="crud-product"),
]