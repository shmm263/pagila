import django_tables2 as tables
from .models import FilmList


class FilmTables(tables.Table):

    class Meta:
        model = FilmList
        template_name = 'django_tables2/bootstrap.html'
        # add class="paleblue" to <table> tag
        #attrs = {'class': 'paleblue'}
        #fields = ('first_name', 'addr_city', 'phone_mobile')
        attrs = {"class": "table-striped table-bordered "}