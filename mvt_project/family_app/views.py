from django.shortcuts import render
from .models import Familiar, Amigo
from django.http import HttpResponse
from django.template import loader
import datetime
 

# Create your views here.

def add_familiar(request):
    f_1 = Familiar(nombre="Gabriel", relacion="Padre",
                   telefono="3541000000", email="gabriel@gmail.com",
                   nacimiento=datetime.date(1962, 5, 28))

    f_2 = Familiar(nombre="Claudia", relacion="Madre",
                   telefono="3541111111", email="claudia@gmail.com",
                   nacimiento=datetime.date(1963, 12, 9))

    f_3 = Familiar(nombre="Romina", relacion="Hermana",
                   telefono="3541222222", email="romina@gmail.com",
                   nacimiento=datetime.date(1988, 6, 12))

    f_1.save()
    f_2.save()
    f_3.save()

    dict_familia = {"nombre_1":f_1.nombre, "relacion_1":f_1.relacion, "tel_1":f_1.telefono, "email_1":f_1.email, "nacimiento_1":f_1.nacimiento,
                    "nombre_2":f_2.nombre, "relacion_2":f_2.relacion, "tel_2":f_2.telefono, "email_2":f_2.email, "nacimiento_2":f_2.nacimiento,
                    "nombre_3":f_3.nombre, "relacion_3":f_3.relacion, "tel_3":f_3.telefono, "email_3":f_3.email, "nacimiento_3":f_3.nacimiento}
    
    plantilla = loader.get_template("familiares.html")

    documento = plantilla.render(dict_familia)

    return HttpResponse(documento)


def add_amigo(request):
    a_1 = Amigo(nombre="Emiliano", telefono="3541000000",
                    email="emiliano@gmail.com",
                    nacimiento=datetime.date(1988, 11, 21))

    a_2 = Amigo(nombre="Bartolo", telefono="3541111111",
                    email="bartolo@gmail.com",
                    nacimiento=datetime.date(1987, 7, 9))

    a_3 = Amigo(nombre="Felix", telefono="3541222222",
                    email="felix@gmail.com",
                    nacimiento=datetime.date(1988, 8, 22))

    a_1.save()
    a_2.save()
    a_3.save()

    dict_amigos = {"nombre_1":a_1.nombre, "tel_1":a_1.telefono, "email_1":a_1.email, "nacimiento_1":a_1.nacimiento,
                   "nombre_2":a_2.nombre, "tel_2":a_2.telefono, "email_2":a_2.email, "nacimiento_2":a_2.nacimiento,
                   "nombre_3":a_3.nombre, "tel_3":a_3.telefono, "email_3":a_3.email, "nacimiento_3":a_3.nacimiento}
    
    plantilla = loader.get_template("amigos.html")

    documento = plantilla.render(dict_amigos)

    return HttpResponse(documento)