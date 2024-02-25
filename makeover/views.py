from django.shortcuts import render
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
"Booking will appear faded until confirmed. Phone us if you would like a short-notice appointment.")

    bookings = Booking.objects.all().filter(username = request.user).order_by('-date_of_booking')
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