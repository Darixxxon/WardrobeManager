import os
from django.shortcuts import render

from myproject.settings import *
from .forms import BasesForm, CoatsForm, HatsForm, OvertopsForm, PantsForm, ShoesForm
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
        form = BasesForm(request.POST, request.FILES)
        if form.is_valid():
            new_base = form.save(commit=False)
            path = f'bases/{new_base.brand}_{new_base.size}_{new_base.length}_{new_base.type}_{new_base.colour_1}_{new_base.colour_2}_{new_base.style}.jpg'
            path = path.replace(' ', '_')
            
            file_path = os.path.join(MEDIA_ROOT, path)
            
            if 'image' in request.FILES:
                add_img(request, file_path)
            
            new_base.dir = f'/media/{path}'
            new_base.new = 0
            new_base.save()
            return render(request, 'adding/add_base.html', {'form': form})
    else:
        form = BasesForm()
        context = {'form': form}
    return render(request, 'adding/add_base.html', context)

def add_overtop(request):
    if request.method == 'POST':
        form = OvertopsForm(request.POST, request.FILES)
        if form.is_valid():
            new_overtop = form.save(commit=False)
            path = f'overtops/{new_overtop.brand}_{new_overtop.size}_{new_overtop.type}_{new_overtop.colour_1}_{new_overtop.colour_2}_{new_overtop.style}.jpg'
            path = path.replace(' ', '_')
            
            file_path = os.path.join(MEDIA_ROOT, path)
            
            if 'image' in request.FILES:
                add_img(request, file_path)
            
            new_overtop.dir = f'/media/{path}'
            new_overtop.new = 0
            new_overtop.save()
            return render(request, 'adding/add_overtop.html', {'form': form})
    else:
        form = OvertopsForm()
        context = {'form': form}
    return render(request, 'adding/add_overtop.html', context)

def add_coat(request):
    if request.method == 'POST':
        form = CoatsForm(request.POST, request.FILES)
        if form.is_valid():
            new_coat = form.save(commit=False)
            path = f'coats/{new_coat.brand}_{new_coat.size}_{new_coat.type}_{new_coat.style}_{new_coat.colour_1}_{new_coat.colour_2}.jpg'
            path = path.replace(' ', '_')
            
            file_path = os.path.join(MEDIA_ROOT, path)
            
            if 'image' in request.FILES:
                add_img(request, file_path)
            
            new_coat.dir = f'/media/{path}'
            new_coat.new = 0
            new_coat.save()
            return render(request, 'adding/add_coat.html', {'form': form})
    else:
        form = CoatsForm()
        context = {'form': form}
    return render(request, 'adding/add_coat.html', context)

def add_hat(request):
    if request.method == 'POST':
        form = HatsForm(request.POST, request.FILES)
        if form.is_valid():
            new_hat = form.save(commit=False)
            path = f'hats/{new_hat.brand}_{new_hat.size}_{new_hat.type}_{new_hat.colour_1}_{new_hat.colour_2}.jpg'
            path = path.replace(' ', '_')
            
            file_path = os.path.join(MEDIA_ROOT, path)
            
            if 'image' in request.FILES:
                add_img(request, file_path)
            
            new_hat.dir = f'/media/{path}'
            new_hat.new = 0
            new_hat.save()
            return render(request, 'adding/add_hat.html', {'form': form})
    else:
        form = HatsForm()
        context = {'form': form}
    return render(request, 'adding/add_hat.html', context)