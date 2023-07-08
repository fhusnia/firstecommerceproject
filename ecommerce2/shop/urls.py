from django.urls import path,include
from . import views



app_name = 'shop'

urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.productlist,name='product_list'),
    path('products/<int:pk>/<str:slug>/',views.productdetail,name='product-detail'),
    path('review/<int:pk>/',views.review,name="review"),
]
