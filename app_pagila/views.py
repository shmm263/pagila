from django.shortcuts import render
from django.views import generic
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from app_pagila.filters import PosteFilter
from app_pagila.tables import FilmTables
from .models import Film, Category, Customer, FilmList



def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_films = Film.objects.all().count()
    num_categories = Category.objects.all().count()
    num_customers = Customer.objects.count()  # Метод 'all()' применен по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_films': num_films, 'num_categories': num_categories,
                 'num_customers': num_customers},
    )

class FilmListView(generic.ListView):
    model = FilmList
    template_name = 'app_pagila/film_list.html'
    paginate_by = 100

class CustomerListView(generic.ListView):
    model = Customer
    template_name = 'app_pagila/custumer_list.html'
    paginate_by = 100


class FilmListView1(SingleTableMixin, FilterView):
    table_class = FilmTables
    model = FilmList
    template_name = 'app_pagila/filmtbl_list.html'
    filterset_class = PosteFilter
    table_pagination = {
        'per_page': 25
    }
