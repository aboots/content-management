from django.urls import path
from rest_framework.routers import DefaultRouter

from contentmanagement import views_api

router = DefaultRouter()

router.register('user', views_api.UserModelViewSet)
router.register('library', views_api.LibraryModelViewSet)

urlpatterns = [
    path('login/', views_api.LoginView.as_view()),
    path('share-library/', views_api.ShareLibraryView.as_view()),
    path('logout/', views_api.LogoutView.as_view()),
]

urlpatterns += router.urls
