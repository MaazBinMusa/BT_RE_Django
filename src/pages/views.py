from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.all().filter(is_published = True)[:3]
    context  = {
        'listings' : listings
    }
    return render(request,'pages/index.html',context)

def about(request):

    context = {
        "realtors" : Realtor.objects.all(),
        'realtors2': Realtor.objects.all()
    }
    return render(request,'pages/about.html',context)