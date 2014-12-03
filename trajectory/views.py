from django.http import HttpResponse
from django.shortcuts import render
from places.models import Place
import requests
import json

# Create your views here.
graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
        'edges': set([
            (1, 'A', 'B'),
            (5, 'A', 'C'),
            (3, 'A', 'D'),
            (4, 'B', 'C'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
        }
minimum_spanning_tree = set([
            (1, 'A', 'B'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
parent = dict()
rank = dict()
sets = set()
places = Place.objects.all()

def getDistance(place1, place2, mode):
    payload = {'origins': place1, 'destinations': place2, 'mode': mode, 'key': 'AIzaSyCdCWqvACnEnbnpzIOT-ga2OO4CobvhsCo'}
    r = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json', params=payload)
    return json.dumps(r.json())

def index(request):
    result = kruskal(graph)
#    assert result == minimum_spanning_tree
    output = str(graph) + "<br>" + str(result)
    for p in places:
        output += "<br>" + p.address
    output += "<br>" + str(getDistance(places[2].address, places[1].address, 'driving'))
    return HttpResponse(output)

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
#    if parent[vertice] != vertice:
#        parent[vertice] = find(parent[vertice])
#    return parent[vertice]
    for item in sets:
        if vertice in item:
            return item

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        tup1 = find(vertice1)
        tup2 = find(vertice2)
        if tup1 is not None and tup1 == tup2:
            continue
        if tup1 is not None:
            if tup2 is not None:
                sets.remove(tup1)
                sets.remove(tup2)
                tup = tup1 + tup2
            else:
                sets.remove(tup1)
                tup = tup1 + vertice2
        elif tup2 is not None:
            sets.remove(tup2)
            tup = tup2 + vertice1
        else:
            tup = (vertice1, vertice2)
        sets.add(tup)

#            union(vertice1, vertice2)
#            minimum_spanning_tree.add(edge)
#    return minimum_spanning_tree
    return sets

