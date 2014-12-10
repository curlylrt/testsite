from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render

from places.models import Place

# Create your views here.
def index(request):
    place_list = Place.objects.order_by('name')
    template = loader.get_template('places/index.html')
    context = RequestContext(request, {'place_list': place_list,})
    return HttpResponse(template.render(context))

def detail(request, place_id):
    try:
        place = Place.objects.get(pk=place_id)
        image_list = place.images.all();
    except Place.DoesNotExist:
        raise Http404
    return render(request, 'places/detail.html', {'place': place,'image_list':image_list})
