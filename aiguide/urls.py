from django.urls import path
from . import views

urlpatterns = [
    path('i/', views.index1, name='index1'),  # URL for the home page with the Figma iframe
]
