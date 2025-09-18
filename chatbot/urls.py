from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('upload/', views.upload_pdf, name='upload_pdf'),
]