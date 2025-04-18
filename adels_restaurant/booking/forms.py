from django import forms
from .models import Booking
from datetime import datetime, timedelta

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_date', 'booking_time', 'number_of_guests', 'special_requests']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date', 'min': datetime.now().date().strftime('%Y-%m-%d')}),
            'booking_time': forms.TimeInput(attrs={'type': 'time'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('booking_date')
        booking_time = cleaned_data.get('booking_time')
        number_of_guests = cleaned_data.get('number_of_guests')
        
        # Validate booking date is not in the past
        if booking_date and booking_date < datetime.now().date():
            raise forms.ValidationError("Booking date cannot be in the past.")
        
        # Validate booking time is within restaurant hours (e.g., 10 AM to 10 PM)
        if booking_time:
            opening_time = datetime.strptime('10:00', '%H:%M').time()
            closing_time = datetime.strptime('22:00', '%H:%M').time()
            if booking_time < opening_time or booking_time > closing_time:
                raise forms.ValidationError("Booking time must be between 10:00 AM and 10:00 PM.")
        
        # Validate number of guests
        if number_of_guests and (number_of_guests < 1 or number_of_guests > 20):
            raise forms.ValidationError("Number of guests must be between 1 and 20.")
        
        return cleaned_data

