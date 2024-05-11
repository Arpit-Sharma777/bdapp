from django.urls import path,re_path
from . import views
#from .views import register, donor_detail
from django.shortcuts import render

urlpatterns = [
    path('', views.donor_list, name='donor_list'),
    path('donor/<int:pk>/', views.donor_detail, name='donor_detail'),
  
    path('register/', views.register_donor, name='register_donor'),
    re_path('search', lambda request: render(request, 'search.html'), name='search'),
]