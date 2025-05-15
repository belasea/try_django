
from . import views
from django.urls import path

urlpatterns = [
   path('get_pdf_file/', views.get_pdf_file, name="get_pdf_file")
]