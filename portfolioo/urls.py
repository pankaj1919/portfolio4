from django.urls import path
from .views import *
from index .urls import *

urlpatterns = [
    path('add_portfolio', addportfolio, name="addportfolio"),
    path('update_portfolio/<pk>',updateportfolio, name='updateportfolio'),
    path('delete_portfolio/<pk>', deleteportfolio, name="deleteportfolio"),
    path('add_category_portfolio', addcategoryportfolio, name="addcategoryportfolio"),
    path('update_category_portfolio/<pk>',updatecategoryportfolio, name='updatecategoryportfolio'),
    path('delete_category_portfolio/<pk>', deletecategoryportfolio, name="deletecategoryportfolio"),
]
