from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Listing

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
    return render(request,'listings/listing.html',{})

def search(request):
    return render(request,'listings/search.html',{})
