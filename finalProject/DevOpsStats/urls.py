from django.urls import path

from . import views

urlpatterns = [

    # original paths
    path("", views.index, name='Index'),
    path("dashboard/", views.dashboard, name='Dashboard'),
    path("redirect", views.redirect, name='Redirect'),
    path("dashboard/new_recommendation", views.new_recon, name='New_Recon'),
    path("error", views.er404, name='Not Found'),

    # project paths
    path("dashboard/reactjs", views.reactjs, name='ReactJS'),
    path("dashboard/data_analytics", views.data_analytics, name='Data_Analytics'),
    path("dashboard/data_science", views.data_science, name='Data_Science'),
    path("dashboard/django", views.django, name='Django'),
    path("dashboard/flask", views.flask, name='Flask'),
    path("dashboard/machine_learning", views.machine_learning, name='Machine_Learning'),
    path("dashboard/nextjs", views.nextjs, name="NextJS"),
    path("dashboard/vuejs", views.vuejs, name='VueJS')


]