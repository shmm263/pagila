from django.shortcuts import render
from django.views import generic

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

class CustomerListView(generic.ListView):
    model = Customer
    template_name = 'app_pagila/custumer_list.html'