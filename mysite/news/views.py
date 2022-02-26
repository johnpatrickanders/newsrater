# from django.shortcuts import render
from .parser import ParseArticles
# Create your views here.

from django.http import HttpResponse


def index(request):
    ParseArticles().save_feed_entries()
    return HttpResponse("Hello, world. You're at the articles index.")
