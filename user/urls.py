
from django.urls import path
from .views import RegisterOrganization, RegisterUser

urlpatterns = [
    path('register_org/', RegisterOrganization.as_view(), name='register_organization'),
    path('register_user/', RegisterUser.as_view(), name='register_user'),
]