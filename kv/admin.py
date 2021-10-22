from django.contrib import admin
from .models import apartments, commercial, zayavki, parking

# Register your models here.


class apartmentsAdmin(admin.ModelAdmin):
    list_display = ("floor", "number_of_bedrooms", "area", "available")
    list_filter = ("floor",)
    fields = ("available",)


class parkingAdmin(admin.ModelAdmin):
    list_display = ("spot", "available")
    list_filter = ("available",)
    fields = ("available",)


class commercialAdmin(admin.ModelAdmin):
    list_display = ("floor", "area", "available")
    list_filter = ("available",)
    fields = ("available",)

class zayavkiAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "phone_number", "date_created")
    # fields = ("available",)


admin.site.register(apartments, apartmentsAdmin)
admin.site.register(commercial, commercialAdmin)
admin.site.register(zayavki, zayavkiAdmin)
admin.site.register(parking, parkingAdmin)
