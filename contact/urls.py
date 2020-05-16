from django.urls import path
from .views import *

urlpatterns = [
    path('addcontact/', addcontact, name="addcontact"),
    path('update_contact/<pk>',updatecontact, name='updatecontact'),
    path('delete_contact/<pk>', deletecontact, name="deletecontact"),
]