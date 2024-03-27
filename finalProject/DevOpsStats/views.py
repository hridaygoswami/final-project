from django.shortcuts import render
from django.http import HttpResponse
from random import randint
# Create your views here.


def index(request):
    # return HttpResponse("Everything is fine?")
    file_path = randint(1, 2)
    return render(request, f"index{file_path}.html")

def dashboard(request):
    return render(request, "dashboard.html")


def redirect(request):
    link = request.POST['name']
    print(link)
    return HttpResponse("Redirecting...")
