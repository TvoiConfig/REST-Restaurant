from django.contrib import admin
from database.models import Dishes, Address, Restaurant, Orders


admin.site.register(Dishes)
admin.site.register(Address)
admin.site.register(Restaurant)
admin.site.register(Orders)
