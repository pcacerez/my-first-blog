from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.utils import timezone # Utilizaremos published_date__lte
from .forms import PostForm
from .models import Post


#.models = el punto indica que estamos en el directorio mimso que realizamos la llamada, en este caso llamos a
# models desde views.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #ordenamos los objetos.
    return render(request, 'conecta/post_list.html', {'posts':posts}) #'posts' = nombre de la varialbe que enviamos.

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'conecta/post_detail.html', {'post': post})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            #guardamos el formulario con form.save
            post = form.save(commit=False)
            #añadimos el autor
            post.author = request.user
            #Lo publicamos, opcional.
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail' , pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'conecta/post_edit.html', {'form': form ,})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'conecta/post_edit.html', {'form': form})
