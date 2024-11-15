from django.contrib import admin
from django.urls import path
from book.views import past_month_list

urlpatterns = [
    path('list/',past_month_list, name='list'),
]