from django.conf.urls import url#Importamos metodos django:
from .views import viewUser
from .views import viewPost
from .views import viewIndex

urlpatterns = [
    url(r'^$', viewIndex.index, name='index'),
    # user=>
    url(r'^user/list$', viewUser.user_list, name='user_list'),
    url(r'^user/(?P<pk>[0-9]+)/$', viewUser.user_detail, name='user_detail'),
    url(r'^user/new/$', viewUser.user_new, name='user_new'),
    url(r'^user/(?P<pk>[0-9]+)/edit/$', viewUser.user_edit, name='user_edit'),
    # post=>
    url(r'^post/list$', viewPost.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', viewPost.post_detail, name='post_detail'),
    url(r'^post/new/$', viewPost.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', viewPost.post_edit, name='post_edit'),
]
# post/ = Significa que después del comienzo, la dirección URL debe contener la palabra post y /
# (?P<pk>[0-9]+) = Significa que Django llevará todo lo que coloques aquí y lo transferirá
# a una vista como una variable llamada pk. [0-9]
# también nos dice que sólo puede ser un número, no una letra (todo debería estar entre 0 y 9).
# + significa que tiene que haber uno o más dígitos. Entonces
# / - entonces necesitamos / de nuevo
# $ - ¡"el final"!
# Example= http://127.0.0.1:8000/post/5/
