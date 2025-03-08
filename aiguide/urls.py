from django.urls import path
from . import views
from .views import CustomLoginView


   

urlpatterns = [
    path('i/', views.inde, name='inde'),  # URL for the home page with the Figma iframe 
       path('login/', CustomLoginView.as_view(), name='login'),
<<<<<<< HEAD
       

=======
       path('signup/', views.signup, name='signup'),
>>>>>>> 0c10f707c0b69e85d6dfe0d32f41c3c1d50b32ad
]

