from django.shortcuts import render, get_object_or_404
from .models import Flower, Type

def all_flowers(request):
    flowers = Flower.objects.all()
    return render(request, 'flowers/all_flowers.html', {'flowers': flowers})

def flowers_by_type(request, type_id):
    flowers = Flower.objects.filter(type_id=type_id)
    type_obj = get_object_or_404(Type, id=type_id)
    return render(request, 'flowers/flowers_by_type.html', {'flowers': flowers, 'type': type_obj})

def single_flower(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    return render(request, 'flowers/single_flower.html', {'flower': flower})
