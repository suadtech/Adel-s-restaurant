from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking, Table
from .forms import BookingForm
from datetime import datetime

@login_required
def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            
            # Find available table based on capacity and time
            number_of_guests = form.cleaned_data['number_of_guests']
            booking_date = form.cleaned_data['booking_date']
            booking_time = form.cleaned_data['booking_time']
            
            # Get tables with sufficient capacity
            suitable_tables = Table.objects.filter(capacity__gte=number_of_guests).order_by('capacity')
            
            # Check which tables are available at the requested time
            available_table = None
            for table in suitable_tables:
                # Check if table is already booked at the requested time
                existing_booking = Booking.objects.filter(
                    table=table,
                    booking_date=booking_date,
                    booking_time=booking_time,
                    status__in=['pending', 'confirmed']
                ).exists()
                
                if not existing_booking:
                    available_table = table
                    break
            
            if available_table:
                booking.table = available_table
                booking.save()
                messages.success(request, "Booking created successfully!")
                return redirect('booking_list')
            else:
                messages.error(request, "No tables available at the requested time. Please try a different time or date.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = BookingForm()
    
    return render(request, 'booking/booking_form.html', {'form': form})

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date', '-booking_time')
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

@login_required
def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    return render(request, 'booking/booking_detail.html', {'booking': booking})

@login_required
def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    
    # Don't allow editing of past bookings
    if booking.booking_date < datetime.now().date():
        messages.error(request, "Cannot edit past bookings.")
        return redirect('booking_list')
    
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking updated successfully!")
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    
    return render(request, 'booking/booking_form.html', {'form': form, 'is_update': True})

@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    
    # Don't allow deleting of past bookings
    if booking.booking_date < datetime.now().date():
        messages.error(request, "Cannot cancel past bookings.")
        return redirect('booking_list')
    
    if request.method == 'POST':
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, "Booking cancelled successfully!")
        return redirect('booking_list')
    
    return render(request, 'booking/booking_confirm_delete.html', {'booking': booking})

