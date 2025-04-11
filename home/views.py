from django.shortcuts import render
from django.urls import reverse
from . models import Header, About, About_Subsection, Service, Destination ,Packages, HeaderImages

# Create your views here.
def home(request):
    header = Header.objects.all()
    header_img = HeaderImages.objects.all()
    about = About.objects.all()
    about_Subsection = About_Subsection.objects.all()
    service = Service.objects.all()
    destination = Destination.objects.all()
    package = Packages.objects.all()

    context = {
        'header' : header,
        'header_img' : header_img,
        'about' : about,
        'about_Subsection' : about_Subsection,
        'service' : service,
        'destination' : destination,
        'package' : package,
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def package(request):
    return render(request, 'package.html')

def contact(request):
    return render(request, 'contact.html')