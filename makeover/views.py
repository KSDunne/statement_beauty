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
    View to edit booking
    """
    if request.method == "POST":
        queryset = Booking.objects.all().filter(username = request.user).order_by('-date_of_booking')
        booking = get_object_or_404(queryset)
        booking = get_object_or_404(Booking, pk=booking_id)
        booking_form = BookingForm(data=request.POST, instance=booking)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.booking = booking
            booking.confirmed = False
            booking.save()
            messages.add_message(request, messages.SUCCESS, 'Booking Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating booking!')

    booking_form = BookingForm()           

    return HttpResponseRedirect(reverse('makeover'))