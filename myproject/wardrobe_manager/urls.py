from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('tables/', show_tables, name='show_tables'),
    path('add/', add_item, name='add_item'),
    path('add_shoes/', add_shoes, name='add_shoes'),
    path('add_pants/', add_pants, name='add_pants'),
    path('add_base/', add_base, name='add_base'),
    path('add_overtop/', add_overtop, name='add_overtop'),
    path('add_coat/', add_coat, name='add_coat'),
    path('add_hat/', add_hat, name='add_hat'),
]
 