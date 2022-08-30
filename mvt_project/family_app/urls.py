from django.urls import path
from family_app.views import *

urlpatterns = [
    path('add_familiar/', add_familiar),
    path('add_amigo/', add_amigo),
    path('mostrar_familiares/', mostrar_familiares),
    path('mostrar_amigos/', mostrar_amigos),
]