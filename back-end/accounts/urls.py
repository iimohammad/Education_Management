from django.urls import path, reverse_lazy
from .views import google_auth_redirect, google_auth_callback
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic.base import RedirectView
from .views import LogoutAPIView, RegisterUserApi

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogoutAPIView.as_view()),
    path('', RegisterUserApi.as_view()),

    # Google Login
    path('google-auth/', google_auth_redirect, name='google_auth_redirect'),
    path('google-auth/redirect/', google_auth_callback, name='google_auth_callback'),

]
