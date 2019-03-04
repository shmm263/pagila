from django.conf.urls import include, url
from .import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^film_list/$', views.FilmListView1.as_view(), name='flist'),
    url(r'^customer_list/$', views.CustomerListView1.as_view(), name='clist'),
]