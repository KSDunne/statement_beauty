from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Makeover, Booking
from .forms import BookingForm


@login_required
def makeover_deals(request):
    """
    Renders the Makeover page
    """
    makeover = Makeover.objects.all().order_by('-updated_on').first()
    
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            bookings = booking_form.save(commit=False)
            bookings.username = request.user
            bookings.save()
            messages.add_message(request, messages.SUCCESS, 
"Booking submitted! It will appear faded until confirmed. Phone us if you would like a short-notice appointment.")

    else:
        booking_form = BookingForm()

    bookings = Booking.objects.all().filter(username=request.user).order_by('date_of_booking')

    return render(
        request,
        "makeover/makeover.html",
        {
            "makeover": makeover,
            "bookings": bookings,
            "booking_form": booking_form,
        },
    )
    
@login_required
def booking_edit(request, booking_id):
    """
    view to edit booking
    """
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking.confirmed = False
            form.save()
            messages.success(request, 'Booking updated successfully.')
            return redirect('makeover')  
    else:
        form = BookingForm(instance=booking)
    return render(request, 'makeover.html', {'form': form, 'booking_id': booking_id})

@login_required
def delete_booking(request, booking_id):
    """
    view to delete booking
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.username == request.user:
        booking.delete()
        messages.add_message(request, messages.SUCCESS, 'Booking deleted!')
        return redirect('makeover') 
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own booking!')
    return render(request, 'makeover.html')