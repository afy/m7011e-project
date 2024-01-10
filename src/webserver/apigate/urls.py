from django.urls import path
from . import views

urlpatterns = [
    # CRUD for all DB tables
    path('product/<int:id>/', views.handle_product_crud, name="crud-product"),
    path('category/<str:name>/', views.handle_category_crud, name="crud-category"),
    path('user', views.handle_user_crud, name='crud-user'),
    path('user/<int:id>/', views.handle_user_crud, name='crud-user'),
    path('verify-token/', views.verify_token, name="verify-token"),
]