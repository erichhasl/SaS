from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'startpage/index.html', {})


def impressum(request):
    return render(request, 'startpage/impressum.html')


def banned(request):
    return render(request, 'startpage/bann.html')
