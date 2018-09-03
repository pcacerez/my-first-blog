from django import forms
#llamamos a nuestro modelo, al estar en el mismo nivel, se indica con un punto. delante de models
from .models.modelPost import Post
#Nombre del formulario.
class PostForm(forms.ModelForm):
#Decimos a Django qué modelo debe utilizar para crear este formulario (model = Post).Configuramos nuestro tipo de formulario...
    class Meta:
        model = Post
        fields = ('author','title', 'text',)
