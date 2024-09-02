from django.contrib import admin
from .models import Rooms,Booking
admin.site.register(Rooms)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','cus_name','cus_phone','cus_email','room_type','book_date','booked_on')
admin.site.register(Booking,BookingAdmin)


