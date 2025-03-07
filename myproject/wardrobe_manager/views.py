from django.shortcuts import render
from .models import Bases, Coats, Combinations, Hats, Overtops, Pants, Shoes

CATEGORY_MODELS = {
    "bases": Bases,
    "coats": Coats,
    "hats": Hats,
    "overtops": Overtops,
    "pants": Pants,
    "shoes": Shoes,
}

def home(request):
    return render(request, 'home.html')

def show_tables(request):
    context = {
        'bases': Bases.objects.all(),
        'coats': Coats.objects.all(),
        'hats': Hats.objects.all(),
        'overtops': Overtops.objects.all(),
        'pants': Pants.objects.all(),
        'shoes': Shoes.objects.all(),
        'combinations': Combinations.objects.all(),
    }
    return render(request, 'tables.html', context)

def add_item(request):
    return render(request, 'adding/add_item.html')