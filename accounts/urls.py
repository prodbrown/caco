from django.conf import settings
from django.conf.urls.static import static
from .views import download_users_csv

from django.urls import path
from .views import register, login, logout, user_list, edit_user, delete_user
from . import views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    # Add other paths here

    path('profile/', views.profile_view, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),


    path('users/', user_list, name='user_list'),
    path('users/edit/<int:user_id>/', edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),


    path('download-users/', download_users_csv, name='download_users_csv'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

