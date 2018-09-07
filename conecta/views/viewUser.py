from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from conecta.forms import UserForm

#.models = el punto indica que estamos en el directorio mimso que realizamos la llamada, en este caso llamos a
# models desde views.

def user_list(request):
    users = User.objects.all() #ordenamos los objetos.
    return render(request, 'user/userList.html', {'users':users,'link':0}) #'posts' = nombre de la varialbe que enviamos.

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user/userDetail.html', {'user': user})

def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            #guardamos el formulario con form.save
            user = form.save(commit=False)
            #añadimos el autor
            #Lo publicamos, opcional.
            user.save()
            return redirect('user_detail' , pk=user.pk)
    else:
        form = UserForm()
        return render(request, 'user/userEdit.html', {'form': form ,'new':1})

def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm(instance=user)
        return render(request, 'user/userEdit.html', {'form': form,'new':0})
