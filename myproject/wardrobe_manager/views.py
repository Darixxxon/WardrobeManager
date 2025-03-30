import os
from django.forms import BaseForm
from django.shortcuts import render

from myproject.settings import *
from .forms import PantsForm, ShoesForm
from .models import Bases, Coats, Combinations, Hats, Overtops, Pants, Shoes
from .functions import *

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
    if request.method == 'POST':
        form = ShoesForm(request.POST, request.FILES)
        if form.is_valid():
            new_shoes = form.save(commit=False)
            path = f'shoes/{new_shoes.brand}_{new_shoes.model}_{new_shoes.size}_{new_shoes.colour_1}_{new_shoes.colour_2}.jpg'
            path = path.replace(' ', '_')
            
            file_path = os.path.join(MEDIA_ROOT, path)
            
            if 'image' in request.FILES:
                add_img(request, file_path)
            
            new_shoes.dir = f'/media/{path}'
            new_shoes.new = 0
            new_shoes.save()
            return render(request, 'adding/add_shoes.html', {'form': form})
    else:
        form = ShoesForm()
        context = {'form': form}
    return render(request, 'adding/add_shoes.html', context)

def add_pants(request):
    if request.method == 'POST':
        form = PantsForm(request.POST, request.FILES)
        if form.is_valid():
            new_pants = form.save(commit=False)
            path = f'pants/{new_pants.brand}_{new_pants.size}_{new_pants.length}_{new_pants.type}_{new_pants.colour_1}_{new_pants.colour_2}_{new_pants.style}.jpg'
            path = path.replace(' ', '_')
            
            file_path = os.path.join(MEDIA_ROOT, path)
            
            if 'image' in request.FILES:
                add_img(request, file_path)
            
            new_pants.dir = f'/media/{path}'
            new_pants.new = 0
            new_pants.save()
            return render(request, 'adding/add_pants.html', {'form': form})
    else:
        form = PantsForm()
        context = {'form': form}
    return render(request, 'adding/add_pants.html', context)

def add_base(request):
    if request.method == 'POST':
        form = BaseForm(request.POST, request.FILES)
        if form.is_valid():
            new_base = form.save(commit=False)
            path = f'base/{new_base.brand}_{new_base.size}_{new_base.length}_{new_base.type}_{new_base.colour_1}_{new_base.colour_2}_{new_base.style}.jpg'
            path = path.replace(' ', '_')
            
            file_path = os.path.join(MEDIA_ROOT, path)
            
            if 'image' in request.FILES:
                add_img(request, file_path)
            
            new_base.dir = f'/media/{path}'
            new_base.new = 0
            new_base.save()
            return render(request, 'adding/add_base.html', {'form': form})
    else:
        form = BaseForm()
        context = {'form': form}
    return render(request, 'adding/add_base.html', context)

def add_overtop(request):
    return render(request, 'adding/add_overtop.html')

def add_coat(request):
    return render(request, 'adding/add_coat.html')

def add_hat(request):
    return render(request, 'adding/add_hat.html')