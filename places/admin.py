from django.contrib import admin
from places.models import Place, PlaceImage

class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 3



class PlaceAdmin(admin.ModelAdmin):
    readonly_fields=('count',)
    inlines = [PlaceImageInline,]

# Register your models here.

admin.site.register(Place, PlaceAdmin)
