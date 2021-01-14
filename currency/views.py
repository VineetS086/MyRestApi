from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import generics, mixins, serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Currency
from .serializers import CurrencySerializer

class CurrencyList(generics.ListAPIView):
    queryset            = Currency.objects.all().order_by('name')
    serializer_class    = CurrencySerializer


class CurrencyListConvert(APIView):

    def get(self, request, code):
        query = Currency.objects.all().order_by('name')
        queryset = []
        for cur in query:

            cur.value/=get_object_or_404(Currency, code=code.upper()).value
            queryset.append(cur)

        serializer = CurrencySerializer(queryset, many=True)
        return Response(serializer.data)


class CurrencyConvert(APIView):
    
    def get(self, request, code, code_2):
        
        currency = get_object_or_404(Currency, code=code_2.upper())
        currency.value /= get_object_or_404(Currency, code=code.upper()).value

        serializer = CurrencySerializer(currency)
        return Response(serializer.data)