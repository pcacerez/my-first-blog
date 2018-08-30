from django.shortcuts import render
from django.utils import timezone # Utilizaremos published_date__lte
from .models import Post

#.models = el punto indica que estamos en el directorio mimso que realizamos la llamada, en este caso llamos a
# models desde views.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #ordenamos los objetos.
    return render(request, 'conecta/post_list.html', {'posts':posts}) #'posts' = nombre de la varialbe que enviamos.
