import django_filters
from .models import FilmList

class PosteFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
       model = FilmList
       fields = {'title', 'category',}