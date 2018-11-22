from django.contrib import admin
from .models import Kitting
from .cellmodel import Cellphone

admin.site.register(Kitting)
admin.site.register(Cellphone)