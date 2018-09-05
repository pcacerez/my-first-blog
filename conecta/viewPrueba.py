from django.shortcuts import render
from .myfunction.mifuncion import prueba

def index(request):
    a=prueba()
    return render(request, 'prueba.html',{'a':a}) #'posts' = nombre de la varialbe que enviamos.
