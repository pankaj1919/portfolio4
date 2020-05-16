from django.urls import path
from .views import *

urlpatterns = [
    path('addeducation/', addeducation, name="addeducation"),
    path('update_education/<pk>',updateeducation, name='updateeducation'),
    path('delete_education/<pk>', deleteeducation, name="deleteeducation"),
    path('addwork/', addwork, name="addwork"),
    path('update_work/<pk>',updatework, name='updatework'),
    path('delete_work/<pk>', deletework, name="deletework"),
    path('addskill/', addskill, name="addskill"),
    path('update_skill/<pk>',updateskill, name='updateskill'),
    path('delete_skill/<pk>', deleteskill, name="deleteskill"),
    path('addtechnical/', addtechnical, name="addtechnical"),
    path('update_technical/<pk>',updatetechnical, name='updatetechnical'),
    path('delete_technical/<pk>', deletetechnical, name="deletetechnical"),
]