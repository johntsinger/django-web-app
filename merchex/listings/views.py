from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing


def hello(request):
    bands = Band.objects.all()
    return render(request,
        "listings/hello.html",
        context={"bands": bands})

def listings(request):
    listings = Listing.objects.all()
    return render(request,
        "listings/listings.html",
        context={"listings": listings})

def about(request):
    return render(request,
        "listings/about.html")

def contact(request):
    return render(request,
        "listings/contact.html")

