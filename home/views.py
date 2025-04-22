from django.shortcuts import render
from django.urls import reverse
from . models import Header, About, Feature, Service, Destination ,Packages, HeaderImages

# Create your views here.
def home(request):
    header = Header.objects.all()
    header_img = HeaderImages.objects.all()
    about = About.objects.all()
    feature = Feature.objects.all()
    service = Service.objects.all()
    destination = Destination.objects.all()
    package = Packages.objects.all()

    context = {
        'header' : header,
        'header_img' : header_img,
        'about' : about,
        'feature' : feature,
        'service' : service,
        'destination' : destination,
        'package' : package,
    }
    return render(request, 'index.html', context)


def about(request):
    about = About.objects.all()
    feature = Feature.objects.all()

    context = {
        'about' : about,
        'feature' : feature,
    }
    return render(request, 'about.html', context)


def service(request):
    return render(request, 'service.html')


def package(request):
    package = Packages.objects.all()
    destination = Destination.objects.all()

    context = {
       'package' : package,
       'destination' : destination, 
    }
    return render(request, 'package.html', context)


def contact(request):
    return render(request, 'contact.html')


def destination(request):
    destination = Destination.objects.all()

    context = {
        'destination' : destination,
    }
    return render(request, 'destination.html', context)