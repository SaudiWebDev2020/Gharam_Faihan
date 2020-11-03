from django.shortcuts import render, HttpResponse ,redirect
from django.http import JsonResponse

def root(request):
    return redirect('./blogs')

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

    
def new(request):
    return HttpResponse ("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/blogs")

def show(request , number):
    return HttpResponse ("placeholder to display blog number: %s" %number)

def edit(request , number):
    return HttpResponse ("placeholder to edit blog: %s" %number)

def destroy(request , number):
    return redirect("/blogs")


def json(request):
    Response ={ "title": "my first Blog" , 
    "content":" My first project in django "}
    return JsonResponse(Response, safe=False)