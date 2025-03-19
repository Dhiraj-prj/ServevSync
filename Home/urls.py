from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from django.urls import path
from .views import houseworker_profile_list, houseworker_profile_detail
from .views import unique_profile_creation_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'), # Display all services
    path('signup/', views.signup, name='signup'),
    path('search/', views.search, name='search'),


    path('login_view/', views.login_view, name='login_view'),

    # Profile related URLs - Keep these distinct
    path('profile/edit/', views.edit_profile, name='edit_profile'), # Edit profile
    path('create-profile/', views.create_profile, name='create_profile'), # Create profile form
    path('unique-create-profile/', unique_profile_creation_view, name='unique_profile_creation_url'),

    # Service related URLs


    path('home/', views.home, name='home'), # Success page after login

    path('houseworker_profiles/', houseworker_profile_list, name='houseworker_profile_list'),
    path('houseworker_profile/<int:profile_id>/', houseworker_profile_detail, name='houseworker_profile_detail'),
    ]

