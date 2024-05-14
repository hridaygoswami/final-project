from django.contrib import admin
from .models import services, collectedData, newServices
# Register your models here.

admin.site.register(services)
admin.site.register(collectedData)
admin.site.register(newServices)