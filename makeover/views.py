from django.shortcuts import render
from .models import Makeover, Booking
from .forms import BookingForm


def makeover_deals(request):
    """
    Renders the Makeover page
    """
    makeover = Makeover.objects.all().order_by('-updated_on').first()
    booking = Booking.objects.all().order_by('-date_of_booking').first()
    booking_form = BookingForm()

    return render(
        request,
        "makeover/makeover.html",
        {
         "makeover": makeover,
         "booking": booking,
         "booking_form": booking_form,
         },
    )