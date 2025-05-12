
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('upload-image/', views.upload_image_view, name='upload-image'),
]