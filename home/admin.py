from django.contrib import admin

# Register your models here.
from .models import*
admin.site.register(Tour)
admin.site.register(Guia)
admin.site.register(Turista)

