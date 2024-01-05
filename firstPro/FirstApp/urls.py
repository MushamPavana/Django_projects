from django.urls import path
from .views import HomePage,signupPage,loginPage,logoutPage

urlpatterns = [
    path('',signupPage, name="signup"),
    path('login/',loginPage, name="login"),
    path('Home/',HomePage, name="Home"),
    path('logout/',logoutPage, name="logout"),
]   
