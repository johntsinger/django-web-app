from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing


def band_list(request):
    bands = Band.objects.all()
    return render(request,
        "listings/band_list.html",
        context={"bands": bands})

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request,
        'listings/band_detail.html',
        {'band': band})

def listing_list(request):
    listings = Listing.objects.all()
    return render(request,
        "listings/listing_list.html",
        context={"listings": listings})

def about(request):
    return render(request,
        "listings/about.html")

def contact(request):
    return render(request,
        "listings/contact.html")

