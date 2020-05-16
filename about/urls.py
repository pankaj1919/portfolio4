from django.urls import path
from .views import *
from index .urls import *

urlpatterns = [
    path('addintro/', addintro, name="addintro"),
    path('update_intro/<pk>',updateintro, name='updateintro'),
    path('delete_intro/<pk>', deleteintro, name="deleteintro"),
    path('addservice/', addservice, name="addservice"),
    path('update_service/<pk>',updateservice, name='updateservice'),
    path('delete_service/<pk>', deleteservice, name="deleteservice"),
    path('addclient/', addclient, name="addclient"),
    path('update_client/<pk>',updateclient, name='updateclient'),
    path('delete_client/<pk>', deleteclient, name="deleteclient"),
    path('addfact/', addfact, name="addfact"),
    path('update_fact/<pk>',updatefact, name='updatefact'),
    path('delete_fact/<pk>', deletefact, name="deletefact"),
    path('addtestomonial/', addtestomonial, name="addtestomonial"),
    path('update_testomonial/<pk>',updatetestomonial, name='updatetestomonial'),
    path('delete_testomonial/<pk>', deletetestomonial, name="deletetestomonial"),
]