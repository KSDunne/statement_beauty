from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
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
    
def booking_edit(request, booking_id):
    """
    Edit an existing booking.

    **Context**

    ``booking``
        An instance of :model:`makeover.Booking`.

    ``booking_form``
        An instance of :form:`makeup.BookingForm`.
    """
    if request.method == "POST":
        booking = get_object_or_404(Booking, pk=booking_id)
        booking_form = BookingForm(data=request.POST, instance=booking)

        if booking_form.is_valid():
            booking = booking_form.save()
            messages.add_message(request, messages.SUCCESS, 'Booking Updated!')
            return HttpResponseRedirect(reverse('makeover', args=[booking_id]))
        else:
            messages.add_message(request, messages.ERROR, 'Error updating booking!')
    else:
        booking = get_object_or_404(Booking, pk=booking_id)
        booking_form = BookingForm(instance=booking)

    return render(request, 'makeover/booking_edit.html', {'booking': booking, 'booking_form': booking_form})
