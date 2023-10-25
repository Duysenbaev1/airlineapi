from django.contrib.admin import *
from .models import Plane, Airlane, Flight

@register(Airlane)
class AirlineAdmin(ModelAdmin):
	list_display = ('id','name')
	list_display_links = ('id','name')

@register(Plane)
class PlaneAdmin(ModelAdmin):
	list_display = ('id','name')
	list_display_links = ('id','name')

@register(Flight)
class FlightAdmin(ModelAdmin):
	list_display = ('id','from_1')
	list_display_links = ('id','from_1')