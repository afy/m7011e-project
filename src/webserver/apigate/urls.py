from django.urls import path
from . import views

urlpatterns = [
    path('prod/get/<str:name>/', views.handle_product_api, kwargs={"func":"get"}, name="get_product"),
    path('prod/update/<str:name>/', views.handle_product_api, kwargs={"func":"update"}, name="update_product"),
]