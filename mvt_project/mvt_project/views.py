from django.http import HttpResponse
from django.template import loader

def saludo(request):
    return HttpResponse("Hola Django")

def template_1(request):

    nom = "Cristian"
    ap = "Torres"
    notas = [2, 5, 8, 6, 4, 1, 9, 3]

    diccionario = {"nombre" : nom, "apellido" : ap, "notas" : notas}

    plantilla = loader.get_template("template_1.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)