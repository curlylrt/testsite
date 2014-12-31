from django.shortcuts import render
from places.models import Place
from menu.forms import OrderForm

# Create your views here.

def index(request):
    place_list = Place.objects.order_by('name')
    form = OrderForm()
    context = {'place_list': place_list, 'form': form}
    return render(request, 'menu/index.html', context)

