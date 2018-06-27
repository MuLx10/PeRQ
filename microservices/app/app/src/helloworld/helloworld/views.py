from django.http import HttpResponse, JsonResponse
import json
import requests

from bot import settings


def index(request):
    return HttpResponse("Hello Hasura World! from Django python2")

