from django.urls import path
from . import views

urlpatterns =[
    path('home', views.home, name = "home"),
    path('logout/', views.logout_req, name= "logout"),
    path("home/signup/", views.SignUp.as_view(), name="signup"),
]