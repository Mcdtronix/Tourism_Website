from django.db import models

# Create your models here.
class Header (models.Model):
    section_title = models.CharField(max_length=255, blank=True, null=True)
    theme = models.TextField()

    def __str__(self):
        return f"{self.section_title} - {self.theme}"

class HeaderImages(models.Model):
    header_img = models.ImageField(upload_to='Assets/header-Images')

    def __str__(self):
        return f"{self.header_img}"

    
class About(models.Model):
    main_img = models.ImageField(upload_to='Assets/About-Images')
    section_title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    img1 = models.ImageField(upload_to='Assets/About-Images')
    img2 = models.ImageField(upload_to='Assets/About-Images')

    def __str__(self):
        return f"{self.section_title} - {self.description}"
    
class Feature(models.Model):
    section_title = models.CharField(max_length=50)
    icon = models.CharField(max_length=255, help_text='should be in form of a string')
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.description}"
    
class Destination(models.Model):
    location = models.CharField(max_length=50)
    sub_title  = models.CharField(max_length=20)
    location_img = models.ImageField(upload_to='Assets/Destination_Images')

    def __str__(self):
        return f"{self.location} - {self.sub_title}"
    
class Service(models.Model):
    icon = models.CharField(max_length=500, help_text='should be in form of a string')
    sub_title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.sub_title} - {self.description}"
    
class Packages(models.Model):
    location = models.CharField(max_length=50)
    period = models.CharField(max_length=20)
    no_of_people = models.CharField(max_length=20)
    description = models.TextField()
    package_img = models.ImageField(upload_to='Assets/Packages_Images')

    def __str__(self):
        return f"{self.no_of_people} - {self.location} - {self.period}"

