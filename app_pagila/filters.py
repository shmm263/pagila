import django_filters
from .models import FilmList, CustomerList

class PosteFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
       model = FilmList
       fields = {'title', 'category',}

class PosteFilter1(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    phone = django_filters.CharFilter(lookup_expr='icontains')
    city  = django_filters.CharFilter(lookup_expr='icontains')
    country = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
       model = CustomerList
       fields = {'name', 'phone', 'city', 'country'}