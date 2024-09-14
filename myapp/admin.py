from django.contrib import admin # type: ignore
from myapp.models import Booking, Room
# Register your models here.

admin.site.register(Booking)
admin.site.register(Room)