from django.shortcuts import render
import math

from .models import ParteiWerbung, PraesidentWerbung


# Create your views here.
def index(request):
    partei_objs = ParteiWerbung.objects.all()
    parteien = group(partei_objs, 3)

    praesident_objs = PraesidentWerbung.objects.all()
    praesidenten = group(praesident_objs, 3)
    return render(request, "news/index.html",
                  {'parteien': parteien, 'praesidenten': praesidenten})


def partei(request, partei_id):
    return render(request, "news/partei.html",
                  {'entry': ParteiWerbung.objects.get(pk=partei_id)})


def praesident(request, praesident_id):
    return render(request, "news/praesident.html",
                  {'entry': PraesidentWerbung.objects.get(pk=praesident_id)})


def group(l, n):
    return [l[k*n:k*n+n] for k in range(math.ceil(len(l) / n))]
