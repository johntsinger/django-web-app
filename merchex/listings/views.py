from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing


def hello(request):
    bands = Band.objects.all()
    return render(request,
        "listings/hello.html",
        {"bands": bands})

def listings(request):
    listings = Listing.objects.all()
    return HttpResponse(f"""
        <h1>Listings</h1>
        <p>Annonces :</p>
        <ul>
            <li>{listings[0].title}</li>
            <li>{listings[1].title}</li>
            <li>{listings[2].title}</li>
        </ul>
    """)

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def contact(request):
    return HttpResponse('<h1>Contactez nous</h1> <p>Formulaire de contact</p>')

