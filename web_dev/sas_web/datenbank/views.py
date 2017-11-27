from django.shortcuts import render
import math

from .models import Entry


# Create your views here.
def index(request):
    query = ""
    if request.method == 'POST':
        query = request.POST['query']
        objects = Entry.objects.filter(title__icontains=query)
    else:
        objects = Entry.objects.all()
    rows = group(objects, 3)
    return render(request, "datenbank/index.html", {'rows': rows,
                                                    'query': query})


def group(l, n):
    return [l[k*n:k*n+n] for k in range(math.ceil(len(l) / n))]
