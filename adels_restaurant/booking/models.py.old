from django.db import models
from django.contrib.auth.models import User
from .table import Table

# Create your models here.
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"

#Booking model
    class Booking(models.Model):
         user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_of_guests = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status_choices = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')
    special_requests = models.TextField(blank=True, null=True)
    
    class Meta:
        # Ensure no double bookings for the same table at the same time
        unique_together = ('table', 'booking_date', 'booking_time')
    
    def __str__(self):
        return f"{self.user.username} - Table {self.table.table_number} - {self.booking_date} {self.booking_time}"
