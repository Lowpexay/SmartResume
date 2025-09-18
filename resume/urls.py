from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_form, name='resume_form'),
    path('pdf/', views.generate_pdf, name='generate_pdf'),
]