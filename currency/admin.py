from django.contrib import admin
from .models import Currency

class CurrencyAdmin(admin.ModelAdmin):
    list_display    = ('name', 'code', 'value', 'last_updated', 'update_status')
    search_fields   = ('name', 'code')
    ordering = ('name',)

admin.site.register(Currency, CurrencyAdmin)
