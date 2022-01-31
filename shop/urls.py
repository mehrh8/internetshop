from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.home, name='search_filter'),
    path('category/<slug:slug>/', views.home, name='category_filter'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
