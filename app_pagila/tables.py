import django_tables2 as tables
from django_tables2 import A

from .models import FilmList, CustomerList


class FilmTables(tables.Table):
    title = tables.LinkColumn('film-detail', args=[A('fid')])
    class Meta:
        model = FilmList
        template_name = 'django_tables2/bootstrap.html'
        # add class="paleblue" to <table> tag
        #attrs = {'class': 'paleblue'}
        #fields = ('first_name', 'addr_city', 'phone_mobile')
        attrs = {"class": "table-striped table-bordered "}

class CustomerTables(tables.Table):
    name = tables.LinkColumn('customer-detail', args=[A('cid')])
    class Meta:
        model = CustomerList
        template_name = 'django_tables2/bootstrap.html'
        # add class="paleblue" to <table> tag
        #attrs = {'class': 'paleblue'}
        fields = ('name', 'address', 'zip_code', 'phone', 'city', 'country', 'notes', 'sid')
        attrs = {"class": "table-striped table-bordered "}