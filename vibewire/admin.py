from django.contrib import admin
from .models import Vibewire

# Register your models here.

vibewire = apps.get_model('vibewire', 'Vibewire')
admin.site.register(Vibewire)
