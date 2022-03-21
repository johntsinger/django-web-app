from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing


def band_list(request):
    bands = Band.objects.all()
    return render(request,
        "listings/band_list.html",
        context={"bands": bands})

def band_detail(request, band_id):
    return render(request,
        'listings/band_detail.html',
        {'band_id': band_id})

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

