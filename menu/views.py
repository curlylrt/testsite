from django.shortcuts import render
from places.models import Place

# Create your views here.

def index(request):
    place_list = Place.objects.order_by('name')
    context = {'place_list': place_list}
    return render(request, 'menu/index.html', context)

