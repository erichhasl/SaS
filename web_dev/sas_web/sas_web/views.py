from django.template.loader import render_to_string
from django.http import (HttpResponseServerError, HttpResponseNotFound,
                         HttpResponseForbidden, HttpResponseBadRequest)


def error_404(request):
    return HttpResponseNotFound(render_to_string('404.html',
                                                 context={'url': request.path}))


def error_500(request):
    return HttpResponseServerError(render_to_string('500.html',
                                                    context={'url': request.path}))


def error_403(request):
    return HttpResponseForbidden(render_to_string('500.html',
                                                  context={'url': request.path}))


def error_400(request):
    return HttpResponseBadRequest(render_to_string('500.html',
                                                   context={'url': request.path}))
