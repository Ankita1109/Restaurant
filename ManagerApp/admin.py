from django.contrib import admin
from .models import ChiefModel,CustomerBill,HomeDelivery,CustomerItems,RecordsManger,Manager
# Register your models here.

@admin.register(ChiefModel)
class ChiefModelAdmin(admin.ModelAdmin):
    list_display=[f.name for f in ChiefModel._meta.fields]
@admin.register(CustomerBill)
class CustomerBillAdmin(admin.ModelAdmin):
    list_display=[f.name for f in CustomerBill._meta.fields]

@admin.register(HomeDelivery)
class HomeDeliveryAdmin(admin.ModelAdmin):
    list_display=[f.name for f in HomeDelivery._meta.fields]

@admin.register(CustomerItems)
class CustomerItemsAdmin(admin.ModelAdmin):
    list_display=[f.name for f in CustomerItems._meta.fields]

@admin.register(RecordsManger)
class RecordsMangerAdmin(admin.ModelAdmin):
    list_display=[f.name for f in RecordsManger._meta.fields]

@admin.register(Manager)
class RecordsMangerAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Manager._meta.fields]