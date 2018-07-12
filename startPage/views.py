from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'startPage/index.html')


def login(request):
    return HttpResponseRedirect('login/index.html')