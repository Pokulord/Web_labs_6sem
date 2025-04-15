from . import views
from django.urls import path, re_path
from blog import views

from django.conf import settings

urlpatterns = [
    path('', views.PostList.as_view(), name= 'home'),
    path('<slug:slug>/', views.PostDetail.as_view() , name='post_detail'),
    re_path(r'^post$', views.PostAPI),
    re_path(r'^post/(.+)$', views.PostAPI)
]