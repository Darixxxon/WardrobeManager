from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('tables/', show_tables, name='show_tables'),
    path('add/', add_item, name='add_item'),
]
 