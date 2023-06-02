from django.shortcuts import render
from .models import Slide, Kitchen, Wardrobe, Bedroom, Furniture

def index(request):
    slide_list = Slide.objects.order_by('sequence')
    kitchen_list = Kitchen.objects.order_by('sequence')
    wardrobe_list = Wardrobe.objects.order_by('sequence')
    bedroom_list = Bedroom.objects.order_by('sequence')
    furniture_list = Furniture.objects.order_by('sequence')
    context = {
        'slide_list': slide_list,
        'kitchen_list': kitchen_list,
        'wardrobe_list': wardrobe_list,
        'bedroom_list': bedroom_list,
        'furniture_list': furniture_list,
    }
    return render(request, 'index.html', context)

# Create your views here.
