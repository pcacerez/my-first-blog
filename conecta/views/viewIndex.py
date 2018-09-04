from django.shortcuts import render

def index(request):
    return render(request, 'index.html') #'posts' = nombre de la varialbe que enviamos.
