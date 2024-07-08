from .views import login, profile
from django.urls import path

urlpatterns = [
    path('auth/login/', login.login_view.as_view(),name='login'),
    path('profile/', profile.profile_view.as_view(),name='profile'),
]