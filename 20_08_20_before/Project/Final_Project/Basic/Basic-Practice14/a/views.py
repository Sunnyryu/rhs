from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    print(request)
    return JsonResponse({'a':'okay'})
# Create your views here.
