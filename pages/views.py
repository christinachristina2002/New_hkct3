from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Page: Pages/Index.html
def index(request):
    #return HttpResponse("<h1>Hello World<h1>")
    return render(request, 'pages/index.html')

#Page: Pages/About.html
def about(request):
    return render(request, 'pages/about.html')

#Page: base.html
def base(request):
    return render(request, 'base.html')