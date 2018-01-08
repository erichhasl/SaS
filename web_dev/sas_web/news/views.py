from django.shortcuts import render
import math

from .models import ParteiWerbung


# Create your views here.
def index(request):
    objects = ParteiWerbung.objects.all()
    rows = group(objects, 3)
    return render(request, "news/index.html", {'rows': rows,
                                               })


def group(l, n):
    return [l[k*n:k*n+n] for k in range(math.ceil(len(l) / n))]
