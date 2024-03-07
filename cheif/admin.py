from django.contrib import admin
from django.db.models import fields


from .models import CheifFood
# Register your models here.

@admin.register(CheifFood)
class ChiefFood(admin.ModelAdmin):
    list_display=[f.name for f in CheifFood._meta.fields]