from django.http import HttpResponse
from django.shortcuts import render
from places.models import Place
from django.views import generic
from django.http import Http404
from django.template.defaulttags import register
import requests
import json

# Create your views here.
output = ""


def getDuration(place1, place2, mode):
    payload = {'origins': place1, 'destinations': place2, 'mode': mode, 'key': 'AIzaSyCdCWqvACnEnbnpzIOT-ga2OO4CobvhsCo'}
    r = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json', params=payload)
    return r.json().get('rows')[0].get('elements')[0].get('duration').get('value')

class IndexView(generic.ListView):
    template_name = 'trajectory/index.html'
    def get_queryset(self):
        return Place.objects.order_by('name')

def index(request):
    place_list = Place.objects.order_by('name')
    context = {'place_list': place_list}
    return render(request, 'trajectory/index.html', context)

@register.filter
def get_place(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_place_name(dictionary, key):
    return dictionary.get(key).name

@register.filter
def get_place_address(dictionary, key):
    return dictionary.get(key).address

@register.filter
def get_place_recommendTime(dictionary, key):
    return dictionary.get(key).recommendTime

@register.filter
def get_place_intro(dictionary, key):
    return dictionary.get(key).intro

def test(request):
    return render(request, 'trajectory/test.html')

def route(request):
    if request.method == 'POST':
        global output
        output = ""
        for x in range(1, 24):
            p = request.POST.getlist(str(x))
            if p is not None:
                for item in p:
                    add = Place.objects.get(pk=item).address
                    output += "<br>" + add
            else:
                break
        output += "<br>The End"
        return HttpResponse(output)


def partition(request):
    if request.method == 'POST':
        edges = list()
        vertices = request.POST.getlist('choice')
        limit = request.POST.get('timeLimit')
        if limit == '':
            limit = 8
        limit = float(limit)
        limit *= 60 * 60
        populate_set(vertices, edges)
        
        result = kruskal(edges, limit)
        selectedPlace = dict()
        for v in vertices:
            selectedPlace[v] = Place.objects.get(pk=v)
        context = {'place_list': selectedPlace, 'sets': result, 'timeLimit': limit}
        return render(request, 'trajectory/result.html', context)

        '''
        global output
        output = ""
        output += "<br>limit: <br>" + str(limit)
        return HttpResponse(output)
        '''
    elif request.method == 'GET':
        vertices = request.GET.getlist('choice')
        output += "<br>request: <br>" + str(vertices)
        return HttpResponse(output)
    raise Http404


def populate_set(vertices, edges):
    if vertices:
        for i in range(1, len(vertices)):
            place1 = Place.objects.get(pk=vertices[i]).address
            for j in range(0, i): 
                place2 = Place.objects.get(pk=vertices[j]).address
                d = getDuration(place1, place2, "driving")
                edges.append((d, vertices[i], vertices[j]))

def find(vertice, sets):
    for item in sets:
        if vertice in item:
            return item

def kruskal(edges, limit):
    edges.sort()
    sets = set();
    for edge in edges:
        duration, vertice1, vertice2 = edge
        tup1 = find(vertice1, sets)
        tup2 = find(vertice2, sets)
        # skip the case where two vertices fall in the same set
        if tup1 is not None and tup1 == tup2:
            continue
        if tup1 is not None:
            if tup2 is not None:
                durSum = tup1[0] + tup2[0] + duration
                if tup1[0] < limit and tup2[0] < limit and durSum < limit:
                    sets.remove(tup1)
                    sets.remove(tup2)
                    tup = (durSum,) + tup1[1:] + tup2[1:]
                else:
                    continue
            else:
                recommendTime2 = Place.objects.get(pk=vertice2).recommendTime * 60 * 60
                durSum = tup1[0] + duration + recommendTime2
                if tup1[0] < limit and durSum < limit:
                    sets.remove(tup1)
                    tup = (durSum, vertice2) + tup1[1:]
                else:
                    tup = (recommendTime2, vertice2)
        elif tup2 is not None:
            recommendTime1 = Place.objects.get(pk=vertice1).recommendTime * 60 * 60

            durSum = tup2[0] + duration + recommendTime1 
            if tup2[0] < limit and durSum < limit:
                sets.remove(tup2)
                tup = (durSum, vertice1) + tup2[1:]
            else:
                tup = (recommendTime1, vertice1)
        else:
            recommendTime1 = Place.objects.get(pk=vertice1).recommendTime * 60 * 60

            recommendTime2 = Place.objects.get(pk=vertice2).recommendTime * 60 * 60

            durSum = duration + recommendTime1 + recommendTime2
            if durSum < limit:
                tup = (durSum, vertice1, vertice2)
            else:
                sets.add((recommendTime1, vertice1))
                sets.add((recommendTime2, vertice2))
                continue
        sets.add(tup)

    return sets

