from django.conf.urls import include, url
from .import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^film_list/$', views.FilmListView1.as_view(), name='flist'),
    url(r'^customer_list/$', views.CustomerListView1.as_view(), name='clist'),
    url(r'^film/(?P<pk>\d+)$', views.FilmDetailView.as_view(), name='film-detail'),
    url(r'^customer/(?P<pk>\d+)$', views.CustomerDetailView.as_view(), name='customer-detail'),
    url(r'^sales_chart/$', views.rainfall_pivot_chart_view, name='saleschart'),
]