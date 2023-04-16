from django.shortcuts import render
from django.http import JsonResponse

def msg_json(request):
    return JsonResponse({"Name": "Hello World!"})

# Create your views here.
