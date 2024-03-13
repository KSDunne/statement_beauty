from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView
from django.contrib import messages

# Credit: https://www.youtube.com/watch?v=JzDBCZTgVyw&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=14
# Credit: https://github.com/Dee-McG/Recipe-Tutorial/blob/main/recipes/views.py#L61
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from .models import Makeover, Booking
from .forms import BookingForm

# Credit: https://github.com/Code-Institute-Solutions/blog/blob/main/12_views_part_3/05_edit_delete/about/views.py#L8
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

    bookings = Booking.objects.all().filter(username=request.user).order_by('date_of_booking', 'start_time')

    return render(
        request,
        "makeover/makeover.html",
        {
            "makeover": makeover,
            "bookings": bookings,
            "booking_form": booking_form,
        },
    )
    
# Credit: https://www.youtube.com/watch?v=JzDBCZTgVyw&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=14
# Credit: https://github.com/Dee-McG/Recipe-Tutorial/blob/main/recipes/views.py#L61
class EditBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a booking"""
    model = Booking
    template_name = 'makeover/edit_makeover.html'
    form_class = BookingForm
    success_url = '/makeover/'
    
    # Credit: https://github.com/DanMorriss/nialls-barbershop/blob/main/booking_system/views.py#L234
    def form_valid(self, form):
        form.instance.confirmed = False
        messages.success(
            self.request,
            "Your booking has been updated!",
            extra_tags="alert alert-success alert-dismissible",
        )

        return super().form_valid(form)
    
    # Credit: https://github.com/DanMorriss/nialls-barbershop/blob/main/booking_system/views.py#L242
    def test_func(self):
        booking = self.get_object()
        return (self.request.user == booking.username or
                self.request.user.is_superuser)


# Credit: https://www.youtube.com/watch?v=JzDBCZTgVyw&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=14
# Credit: https://github.com/Dee-McG/Recipe-Tutorial/blob/main/recipes/views.py#L72
# Credit: https://github.com/DanMorriss/nialls-barbershop/blob/main/booking_system/views.py#L272
class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a recipe"""
    model = Booking
    success_url = '/makeover/'
    
    #def delete(self, request):
    #    booking = self.get_object(booking)
    #    if self.request.user.username:
    #        messages.success(
    #       self.request,
    #       "Your booking has been successfully deleted!",
    #       extra_tags="alert alert-danger alert-dismissible",
    #           )
    #   return super().delete(request)
    
    def test_func(self):
        booking = self.get_object()
        return (self.request.user == booking.username or
                self.request.user.is_superuser)
