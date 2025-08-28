from django.contrib import admin
from .models import Customers, ExistingHtLine, HtLineConstructed, HtPoles, LvPoles, Parcels, SinglePhase
from leaflet.admin import LeafletGeoAdmin


# Register your models here.


class CustomersAdmin(LeafletGeoAdmin):
    list_display = ("customer_s_name", "phone_number", "parcel_number", "power_rate_supply")



class HtPolesAdmin(LeafletGeoAdmin):
    list_display = ("no", "name", "type", "height", "fitting")

class LvPolesAdmin(LeafletGeoAdmin):
    list_display = ("no", "type_string_field", "name_string_field", "height_m_field")


admin.site.register(Customers, CustomersAdmin)
admin.site.register(HtPoles, HtPolesAdmin)
admin.site.register(LvPoles, LvPolesAdmin)
