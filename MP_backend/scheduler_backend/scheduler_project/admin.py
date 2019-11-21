from django.contrib import admin
from .models import Process, Slots, Parameters, Efficiency
# Register your models here.
admin.site.register(Process)
admin.site.register(Slots)
admin.site.register(Parameters)
admin.site.register(Efficiency)

