from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
# BlankOn Views Configuration

def beranda(request, page):
    return render_to_response(page)