from django.urls import path
from . import views
from .views import CustomLoginView


   

urlpatterns = [
    path('i/', views.inde, name='inde'),  # URL for the home page with the Figma iframe 
       path('login/', CustomLoginView.as_view(), name='login'),
       

]

