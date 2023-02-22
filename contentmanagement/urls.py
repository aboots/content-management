from django.urls import path
from rest_framework.routers import DefaultRouter

from contentmanagement import views_api

router = DefaultRouter()

router.register('user', views_api.UserModelViewSet)

urlpatterns = [
    path('login/', views_api.LoginView.as_view()),
    path('logout/', views_api.LogoutView.as_view()),
]

urlpatterns += router.urls
