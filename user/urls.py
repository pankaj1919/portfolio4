from django.urls import path
from .views import *
from index .urls import *

urlpatterns = [
    path("account_settings/", profile, name="profile"),
]