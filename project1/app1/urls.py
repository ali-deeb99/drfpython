from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from . import admin
urlpatterns = [
    path('user-registration',views.UserRegistration.as_view()),
    path('api-token-auth',obtain_auth_token),
    path('f',views.f),
    path('entity-registration',views.RegistrationEntity.as_view()),
    path('send-email',views.index),
]


