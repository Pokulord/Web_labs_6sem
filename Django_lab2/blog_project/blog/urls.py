from . import views
from django.urls import path, re_path,include
from blog import views
from rest_framework.routers import DefaultRouter

from django.conf import settings

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('', views.PostList.as_view(), name= 'home'),
    path('<slug:slug>/', views.PostDetail.as_view() , name='post_detail'),
    path('api/v1/', include(router.urls))
]