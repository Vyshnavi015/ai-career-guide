from django.urls import path
from . import views

urlpatterns = [
    path('\i', views.index, name='index'),  # URL for the home page with the Figma iframe
]
