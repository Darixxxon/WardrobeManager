from django.urls import path
from .views import home, show_tables

urlpatterns = [
    path('', home, name='home'),
    path('tables/', show_tables, name='show_tables'),
]
 