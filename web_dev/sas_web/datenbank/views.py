from django.shortcuts import render
import math

from .models import Entry


# Create your views here.
def index(request):
    rows = group(Entry.objects.all(), 3)
    print("rows", rows)
    return render(request, "datenbank/index.html", {'rows': rows})


def group(l, n):
    return [l[k*n:k*n+n] for k in range(math.ceil(len(l) / n))]
