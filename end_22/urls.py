from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='home'),  # Add this line to handle the empty path
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
]
