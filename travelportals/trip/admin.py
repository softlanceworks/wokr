from django.contrib import admin

from .models import Location,Tour,Categories

# Register your models here.
admin.site.register(Location)
admin.site.register(Tour)
admin.site.register(Categories)
