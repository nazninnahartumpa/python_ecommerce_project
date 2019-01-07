from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('', views.IndexView.as_view(), name= 'index'),
    path('products/', views.ProductList.as_view(), name='products'),
    path('products/search/', views.SearchProductsList.as_view(), name='search'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='detail'),
    path('products/<slug:slug>', views.ProductSlugtDetailView.as_view(), name='detail'),
    path('products/feature/list', views.FeaturedProductList.as_view(),name='featured'),
    path('products/feature/detail/<int:pk>', views.FeaturedProductDetailView.as_view(),name='featured_detail'),


]