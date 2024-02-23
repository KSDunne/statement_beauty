from django.shortcuts import render
from .models import Makeover, Booking
from .forms import BookingForm


def makeover_deals(request):
    """
    Renders the Makeover page
    """
    makeover = Makeover.objects.all().order_by('-updated_on').first()
    bookings = Booking.objects.all().order_by('-date_of_booking')
    
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            bookings = booking_form.save(commit=False)
            bookings.username = request.user
            bookings.save()

    
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