from django.shortcuts import render, HttpResponse
#from ....domain.entities.Categoria import Categoria
# Create your views here.
def index(request):
    print('oi')
    return HttpResponse("You're looking at question")