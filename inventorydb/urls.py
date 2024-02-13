from django.urls import path
from .views import (DownloadCSVView, InventoryViewSet, LoginView, LogoutView,
                    check_authentication, EmailAPI)
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('check-auth/', check_authentication, name='check-authentication'),
    path('login/', LoginView.as_view(),
         name='users-login'),
    #     path('users/', UserListView.as_view(),
    #          name='users-litt'),
    path('logout/', LogoutView.as_view(),
         name='users-logout'),
    path('download-csv/', DownloadCSVView.as_view(), name='download_csv'),
    path('send-email/',  EmailAPI.as_view(),
         name='send-email'),


]

router = DefaultRouter()
router.register(r'inventories', InventoryViewSet, basename='inventory/')
urlpatterns += router.urls
