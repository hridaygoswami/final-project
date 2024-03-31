from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import subprocess
import os 
# Create your views here.

def clone_repo(repo_url, destination_path):
    try:
        subprocess.run(["git", "clone", repo_url, destination_path], check=True)
        print("Clonning successful")
    except subprocess.CalledProcessError as e:
        print(f"Error in cloning {e}")

def folder_size_and_extensions(folder_path):
    total_size = 0
    extensions = set()

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
            _, ext = os.path.splitext(f)
            extensions.add(
                ext.lower()
            )  # Lowercasing to ensure case-insensitive comparison

    return total_size, extensions

def check_for_mern(directory):
    # Check for common files/directories in a MERN stack
    mern_files = ["package.json", "server.js", "client", "public", "src"]
    for file in mern_files:
        if not os.path.exists(os.path.join(directory, file)):
            return False
    return True

def check_for_django(directory):
    # Check for common files/directories in a Django app
    django_files = ["manage.py", "requirements.txt", "myproject"]
    for file in django_files:
        if not os.path.exists(os.path.join(directory, file)):
            return False
    return True


def index(request):
    # return HttpResponse("Everything is fine?")
    file_path = randint(1, 2)
    return render(request, f"index{file_path}.html")

def dashboard(request):
    return render(request, "dashboard.html")


def redirect(request):
    link = request.POST['name']
    data = link.split(".")
    folder_name = data[1].split("/")[1]
    project_name = data[1].split("/")[2]
    path = f"./files/{folder_name}/{project_name}"
    if data[-1] == "git":
        print("GIT url", folder_name)
        clone_repo(link, path)
        (total_size, extensions) = folder_size_and_extensions(path)
        total_size_kb = total_size/1024
        total_size_mb = total_size_kb / 1024
        for i in extensions:
            d = i.split(".")[-1]
            if d == ".jsx":
                print("React")
        print(total_size_mb, extensions)

    else:
        print("Not a valid GIT url")
    return HttpResponse("Redirecting...")
