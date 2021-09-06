from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.core.validators import MinLengthValidator
from .models import Customer
from django.views import View


def index(request):
    return render(request, 'index.html')


def flower(request):
    return render(request, 'flower.html')


def fruits(request):
    return render(request, 'fruits.html')


def timber(request):
    return render(request, 'timber.html')


def herbal(request):
    return render(request, 'herbal.html')


def indoor(request):
    return render(request, 'indoor.html')


def foreign(request):
    return render(request, 'foreign.html')


def spices(request):
    return render(request, 'spices.html')


def vegetable(request):
    return render(request, 'vegetable.html')


def seed(request):
    return render(request, 'seed.html')


def bouquet(request):
    return render(request, 'bouquet.html')


def fertilizer(request):
    return render(request, 'fertilizer.html')


def accessories(request):
    return render(request, 'accessories.html')


def tips(request):
    return render(request, 'tips.html')


def cart(request):
    return render(request, 'cart.html')


def contact(request):
    return render(request, 'contact.html')


def signup(request):
    return render(request, 'singup.html')


def login(request):
    return render(request, 'loging.html')
