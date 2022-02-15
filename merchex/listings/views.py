from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse('<h1>Hello Django !</h1>')

def listings(request):
    return HttpResponse('<h1>Listings</h1> <ul><li>élément 1</li> <li>élément 2</li></ul>')

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def contact(request):
    return HttpResponse('<h1>Contactez nous</h1> <p>Formulaire de contact</p>')

