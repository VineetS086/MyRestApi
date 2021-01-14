from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.CurrencyList.as_view()),
    path('<str:code>/', views.CurrencyListConvert.as_view()),
    path('<str:code>/<str:code_2>/', views.CurrencyConvert.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)


'''from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

'''