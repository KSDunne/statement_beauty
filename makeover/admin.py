from django.contrib import admin
from .models import Makeover, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Makeover)
class MakeoverAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Class to view the Bookings in the admin panel"""
    list_display = ('username',
                    'date_of_booking',
                    'service_type',
                    'start_time',
                    'confirmed')
    list_filter = ('date_of_booking', 'username')
    search_fields = ['username', 'service_type']
    actions = ['confirm_booking']

    def confirm_booking(self, request, queryset):
        queryset.update(confirmed=True)
