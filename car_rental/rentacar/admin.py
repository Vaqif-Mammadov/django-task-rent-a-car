from django.contrib import admin
from .models import Car, Owner, RentACar

# Register your models here.

class OwnerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.clean()
        super().save_model(request, obj, form, change)

admin.site.register(Car)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(RentACar)
