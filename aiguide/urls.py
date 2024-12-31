from django.urls import path
from . import views

urlpatterns = [
    path('i/', views.inde, name='inde'),  # URL for the home page with the Figma iframe
     path('t/', views.tenth, name='10thindex'), 
]
