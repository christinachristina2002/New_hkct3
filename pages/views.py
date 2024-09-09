from django.shortcuts import render
from listings.models import Listing #<-- load listings\models.py
from realtors.models import Realtor #<-- load realtors\models.py
#from django.http import HttpResponse <-- load HTML

# Create your views here.

#Page: Pages/Index.html
def index(request):
    #return HttpResponse("<h1>Hello World<h1>")
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)[:3]
    context = {'listings':listings}
    return render(request, 'pages/index.html', context)

#Page: Pages/About.html
def about(request):
    realtors = Realtor.objects.order_by("-hire_date")
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }
    return render(request, 'pages/about.html', context)

