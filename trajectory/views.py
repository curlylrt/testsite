from django.http import HttpResponse
from django.shortcuts import render
from places.models import Place
from django.views import generic
from django.http import Http404
import requests
import json

# Create your views here.
output = ""


def getDistance(place1, place2, mode):
    payload = {'origins': place1, 'destinations': place2, 'mode': mode, 'key': 'AIzaSyCdCWqvACnEnbnpzIOT-ga2OO4CobvhsCo'}
    r = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json', params=payload)
    return r.json().get('rows')[0].get('elements')[0].get('distance').get('value')

class IndexView(generic.ListView):
    template_name = 'trajectory/index.html'
    def get_queryset(self):
        return Place.objects.order_by('name')

def index(request):
    place_list = Place.objects.order_by('name')
    context = {'place_list': place_list}
    return render(request, 'trajectory/index.html', context)

def partition(request):
    if request.method == 'POST':
        global output
        output = ""
        edges = list()
        vertices = request.POST.getlist('choice')

        populate_set(vertices, edges)
        
        result = kruskal(edges)
        output += "<br>result: <br>" + str(result)
        output += "<br>vertice: <br>" + str(vertices) + "<br>egdes: <br>" + str(edges)

        return HttpResponse(output)
    raise Http404


def populate_set(vertices, edges):
    global output
    if vertices:
        for i in range(1, len(vertices)):
            place1 = Place.objects.get(pk=vertices[i]).address
            for j in range(0, i): 
                place2 = Place.objects.get(pk=vertices[j]).address
                d = getDistance(place1, place2, "driving")
                edges.append((d, vertices[i], vertices[j]))

def find(vertice, sets):
    for item in sets:
        if vertice in item:
            return item

def kruskal(edges):
    edges.sort()
    sets = set();
    for edge in edges:
        weight, vertice1, vertice2 = edge
        tup1 = find(vertice1, sets)
        tup2 = find(vertice2, sets)
        if tup1 is not None and tup1 == tup2:
            continue
        if tup1 is not None:
            if tup2 is not None:
                sets.remove(tup1)
                sets.remove(tup2)
                tup = tup1 + tup2
            else:
                sets.remove(tup1)
                tup = tup1 + (vertice2,)
        elif tup2 is not None:
            sets.remove(tup2)
            tup = tup2 + (vertice1,)
        else:
            tup = (vertice1, vertice2)
        sets.add(tup)

    return sets

