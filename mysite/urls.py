from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('conecta.urls')), #Indicamos a nuestra url del localhost:8000 vaya directamente a conecta
    # r al principio de la cadena indica a Python que la cadena contendrá caracteres especiales.
    # que no son para ser interpretados por Python, sino que son parte de la rexpresión regular.
    ]
