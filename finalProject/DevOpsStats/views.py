from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from random import randint
import subprocess
import os 
# Create your views here.

def detect_technology(file_extensions):
    reactjs_extensions = {".jsx", ".js"}
    nextjs_extensions = {".jsx", ".js", ".tsx", ".ts"}
    vuejs_extensions = {".vue"}
    django_extensions = {".py"}
    flask_extensions = {".py"}
    data_science_extensions = {".ipynb", ".py"}
    data_analytics_extensions = {".sql", ".csv", ".xlsx"}
    machine_learning_extensions = {".ipynb", ".py"}
    
    if any(ext in reactjs_extensions for ext in file_extensions):
        return "reactjs"
    elif any(ext in nextjs_extensions for ext in file_extensions):
        return "nextjs"
    elif any(ext in vuejs_extensions for ext in file_extensions):
        return "vuejs"
    elif any(ext in django_extensions for ext in file_extensions):
        return "django"
    elif any(ext in flask_extensions for ext in file_extensions):
        return "flask"
    elif any(ext in data_science_extensions for ext in file_extensions):
        return "data_science"
    elif any(ext in data_analytics_extensions for ext in file_extensions):
        return "data_analytics"
    elif any(ext in machine_learning_extensions for ext in file_extensions):
        return "machine_learning"
    else:
        return "Unknown"


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
    mern_files = ["package.json", "main.jsx", "client", "public", "src", "App.jsx"]
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
    if data[-1] == "git":
        folder_name = data[1].split("/")[1]
        project_name = data[1].split("/")[2]
        path = f"./files/{folder_name}/{project_name}"
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
        technology = detect_technology(extensions)
        print(technology)
        return HttpResponseRedirect(f"dashboard/{technology}")

    else:
        print("Not a valid GIT url")
    # return HttpResponse("Redirecting...")
    # return HttpResponseRedirect("error")


def new_recon(request):
    return render(request, "new_recommendation.html")



# error page
def er404(request):
    return render(request, "404.html")


# project pages

def reactjs(request):
    return render(request, "projects_types/reactjs.html")

def data_analytics(request):
    return render(request, "projects_types/data_analytics.html")

def data_science(request):
    return render(request, "projects_types/data_science.html")

def django(request):
    return render(request, "projects_types/django.html")

def flask(request):
    return render(request, "projects_types/flask.html")

def machine_learning(request):
    return render(request, "projects_types/machine_learning.html")

def nextjs(request):
    return render(request, "projects_types/nextjs.html")

def vuejs(request):
    return render(request, "projects_types/vuejs.html")