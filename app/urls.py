from django.urls import path
from . import views 





urlpatterns = [
    path('', views.index_page, name='index'),
    path('login/', views.loginpage, name='login'),
    path('register', views.RegisterPage, name='register'),
    path('dashboard', views.Dashboard, name='dashboard'),
    path('about', views.About_page, name='about'),
    path('contact', views.contact, name='contact'),
    
]