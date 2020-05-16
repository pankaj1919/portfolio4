from django.urls import path
from .views import *
from index .urls import *

urlpatterns = [
    path('addhome/', addhome, name="addhome"),
    path('update_home/<pk>',updatehome, name="updatehome"),
    path('delete_home/<pk>', deletehome, name="deletehome"),
]