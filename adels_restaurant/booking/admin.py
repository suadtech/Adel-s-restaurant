from django.contrib import admin
from .models import Table, Booking

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'is_available')
    list_filter = ('is_available', 'capacity')
    search_fields = ('table_number',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'booking_date', 'booking_time', 'number_of_guests', 'status')
    list_filter = ('booking_date', 'status')
    search_fields = ('user__username', 'user__email')
    date_hierarchy = 'booking_date'

