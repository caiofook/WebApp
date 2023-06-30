# importing the classes that this view and it's templates need
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def landing(request):
    return render(request, 'WebApp/base.html') #essa função retorna uma resposta http


def about(request):
    return render(request, 'WebApp/about.html', {'title': 'About'})