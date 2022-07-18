from django.contrib import admin
from .models import Depoimentos


class ListandoDepoimentos(admin.ModelAdmin):
    list_display = ('id', 'nome_depoimento')
    list_display_links = ('id', 'nome_depoimento')
    search_fields = ('nome_depoimento',)
    list_filter = ('nome_depoimento',)
    list_per_page: 5

admin.site.register(Depoimentos, ListandoDepoimentos)
