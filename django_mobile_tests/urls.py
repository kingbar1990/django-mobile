from django.urls import re_path
from django.shortcuts import render_to_response
from django.template import RequestContext
from django_mobile.cache import cache_page


def index(request):
    return render_to_response('index.html', {
    }, context_instance=RequestContext(request))


urlpatterns = [
    re_path(r'^$', index),
    re_path(r'^cached/$', cache_page(60*10)(index)),
]
