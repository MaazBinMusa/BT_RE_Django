from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Listing
from .constants import prices,states,bedrooms

def listings(request):

    listdata  = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listdata,1)
    page      = request.GET.get('page')
    listdata  = paginator.get_page(page)
    context   = {
        "listings":listdata
    }
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):

    listing = get_object_or_404(Listing,pk=listing_id)
    context = {
        'listing' : listing
    }
    return render(request,'listings/listing.html',context)

def search(request):

    listings = Listing.objects.all()

    # Keyword Filter on Form
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(description__icontains=keywords)

    context = {
        'listings' : listings,
        'states': states,
        'bedrooms':bedrooms,
        'prices':prices,
        'values':request.GET
    }
    return render(request,'listings/search.html',context)
