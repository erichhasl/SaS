from django.shortcuts import render
from .models import Parlamentssitzung


# Create your views here.
def index(request):
    sessions = Parlamentssitzung.objects.all()
    return render(request, "news/index.html", {'sessions': sessions})
