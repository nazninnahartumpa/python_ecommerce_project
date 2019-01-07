from django.urls import path
from test_app import views
from django.views.generic import TemplateView

app_name = 'test_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name= 'index'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
    path('login/', views.LoginPage.as_view(), name = 'login'),
    path('register/', views.RegisterPage.as_view(), name = 'register'),
    path('bootstrap/', views.TemplateView.as_view(template_name='bootstrap/example.html') ),

]