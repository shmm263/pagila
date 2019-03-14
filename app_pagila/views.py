from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views import generic
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from app_pagila.filters import PosteFilter, PosteFilter1
from app_pagila.tables import FilmTables, CustomerTables
from .models import Film, Category, Customer, CustomerList, FilmList, Sales_by_store_by_category
from chartit import PivotDataPool, PivotChart
from django.db.models import Sum


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
        'per_page': 13
    }

class CustomerListView1(SingleTableMixin, FilterView):
    table_class = CustomerTables
    model = CustomerList
    template_name = 'app_pagila/customertbl_list.html'
    filterset_class = PosteFilter1
    table_pagination = {
        'per_page': 25
    }

class FilmDetailView(generic.DetailView):
    model = FilmList
    template_name = 'app_pagila/filmlist_detail.html'


class CustomerDetailView(generic.DetailView):
    model = CustomerList
    template_name = 'app_pagila/customerlistr_datail.html'


def rainfall_pivot_chart_view(request):
    #Step 1: Create a PivotDataPool with the data we want to retrieve.
    rainpivotdata = \
        PivotDataPool(
           series =
            [{'options': {
               'source': Sales_by_store_by_category.objects.all(),
               'categories': ['store', 'manager'],
               'legend_by': 'category'},
              'terms': {
                'sum_total_sales': Sum('total_sales'),
                #'legend_by': ['category'],
               # 'top_n_per_cat': 3
              }}])

    #Step 2: Create the PivotChart object
    rainpivcht = \
        PivotChart(
            datasource = rainpivotdata,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': True},
                'terms':[
                  'sum_total_sales']}],
            chart_options =
              {'title': {
                   'text': 'Rain by Month in top 3 cities'},
               'xAxis': {
                    'title': {
                       'text': 'Month'}}})

    #Step 3: Send the PivotChart object to the template.
    return render(request, 'app_pagila/Sales_store_category.html',{'rainpivchart': rainpivcht})