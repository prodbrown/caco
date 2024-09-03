from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),
    
    # Blog Post URLs
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('not_required/', views.not_required, name='not_required'),

    # About URLs
    path('about/', views.about_detail, name='about_detail'),
    path('edit/about/', views.about_edit, name='about_edit'),
    path('delete/about/', views.about_delete, name='about_delete'),

    # Contact URLs
    path('contact/', views.contact_detail, name='contact_detail'),
    path('edit/contact/', views.contact_edit, name='contact_edit'),
    path('delete/contact/', views.contact_delete, name='contact_delete'),

    # Announcement URLs
    path('announcements/', views.announcement_list, name='announcement_list'),
    path('announcement/<int:pk>/', views.announcement_detail, name='announcement_detail'),
    path('create/announcement/', views.announcement_create, name='announcement_create'),
    path('edit/announcement/<int:pk>/', views.announcement_edit, name='announcement_edit'),
    path('delete/announcement/<int:pk>/', views.announcement_delete, name='announcement_delete'),
]
