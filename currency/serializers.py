from rest_framework import serializers
from .models import Currency

class CurrencySerializer(serializers.ModelSerializer):
    # def __init__(self, cur):
    #     val = 1

    value   = serializers.DecimalField(25,9)

    class Meta:
        model = Currency
        fields = ['name', 'code', 'value']
        ordering = ['name']
