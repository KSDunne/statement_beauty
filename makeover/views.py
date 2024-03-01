from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Makeover, Booking
from .forms import BookingForm


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

    bookings = Booking.objects.all().filter(username = request.user).order_by('date_of_booking')
    booking_form = BookingForm()


    return render(
        request,
        "makeover/makeover.html",
        {
         "makeover": makeover,
         "bookings": bookings,
         "booking_form": booking_form,
         },
    )
    
def booking_edit(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking.confirmed = False
            form.save()
            messages.success(request, 'Booking updated successfully.')
            return redirect('makeover')  # Redirect to the makeover page
    else:
        form = BookingForm(instance=booking)
    return render(request, 'makeover.html', {'form': form, 'booking_id': booking_id})