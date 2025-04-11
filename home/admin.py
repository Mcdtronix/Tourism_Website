from django.contrib import admin
from . models import Header, About, About_Subsection, Service, Destination ,Packages, HeaderImages

# Register your models here.
@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('section_title', 'theme')
    list_filter = ('section_title',)
    

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('section_title', 'description')

@admin.register(About_Subsection)
class About_SubsectionAdmin(admin.ModelAdmin):
    list_display = ('section_title', 'icon', 'description')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('sub_title', 'icon')
    
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('location', 'sub_title')
    list_filter = ('location','sub_title')
    search_fields = ('location',)

@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    list_display = ('no_of_people', 'location', 'period', 'description')
    list_filter = ('location', 'no_of_people', 'period',)
    search_fields = ('location', 'no_of_people', 'period')

admin.site.register(HeaderImages)