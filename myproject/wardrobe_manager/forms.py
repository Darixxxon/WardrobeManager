from .models import Bases, Coats, Hats, Overtops, Pants, Shoes
from django import forms

class ShoesForm(forms.ModelForm):
    class Meta:
        model = Shoes
        fields = ['brand', 'model', 'size', 'colour_1', 'colour_2', 'type']
        
class PantsForm(forms.ModelForm):
    class Meta:
        model = Pants
        fields = ['brand', 'size', 'length', 'type', 'colour_1', 'colour_2', 'style', 'dir']
        
class BasesForm(forms.ModelForm):
    class Meta:
        model = Bases
        fields = ['brand', 'size', 'length', 'type', 'colour_1', 'colour_2', 'style', 'dir']
        
class OvertopsForm(forms.ModelForm):
    class Meta:
        model = Overtops
        fields = ['brand', 'size', 'type', 'colour_1', 'colour_2', 'style', 'dir']
        
class CoatsForm(forms.ModelForm):
    class Meta:
        model = Coats
        fields = ['brand', 'size', 'type', 'style', 'colour_1', 'colour_2', 'dir']
    
class HatsForm(forms.ModelForm):
    class Meta:
        model = Hats
        fields = ['brand', 'size', 'type', 'colour_1', 'colour_2', 'dir']
    