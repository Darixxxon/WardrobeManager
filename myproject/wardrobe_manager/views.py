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

def add_shoes(request):
    return render(request, 'adding/add_shoes.html')

def add_pants(request):
    return render(request, 'adding/add_pants.html')

def add_base(request):
    return render(request, 'adding/add_base.html')

def add_overtop(request):
    return render(request, 'adding/add_overtop.html')

def add_coat(request):
    return render(request, 'adding/add_coat.html')

def add_hat(request):
    return render(request, 'adding/add_hat.html')