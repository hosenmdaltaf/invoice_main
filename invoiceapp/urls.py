from django.urls import path
from . import views

app_name='invoiceapp'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('pdf/', views.pdf_generator, name='pdfpage'),
]