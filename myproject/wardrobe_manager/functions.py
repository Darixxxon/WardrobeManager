from PIL import Image
from .models import Bases, Coats, Combinations, Hats, Overtops, Pants, Shoes


def add_img(request, file_path):
    image = request.FILES['image']
    img = Image.open(image)
    img.convert('RGB')
    img.save(file_path, 'JPEG')
    
