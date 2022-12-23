from django.shortcuts import HttpResponse

def index(request,name):
    return HttpResponse(f'<h1> Hell musabbir my name is {name} </h1>')