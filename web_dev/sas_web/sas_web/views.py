from django.template.loader import render_to_string
from django.http import HttpResponseNotFound


def error_404(request):
    return HttpResponseNotFound(render_to_string('404.html',
                                                 context={'url': request.path}))
