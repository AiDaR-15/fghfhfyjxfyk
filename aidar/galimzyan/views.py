from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    x = request.META["HTTP_HOST"]
    # y = request.META["HTTP_HOST"]
    host = request.path

    text = "host"
    return HttpResponse(text)

