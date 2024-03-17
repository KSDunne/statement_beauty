from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.contrib import messages
from .models import Makeover, Booking
from .forms import BookingForm


# Views


# Credit: https://github.com/Code-Institute-Solutions/blog/blob/main/12_views_part_3/05_edit_delete/about/views.py#L8
@login_required
def makeover_deals(request):
    """
    Renders the Makeover page with booking functionality

    **Context**

    ``makeover``
        The most recent instance of :model:`makeover.Makeover`
    ``bookings``
        All bookings made by the current user, ordered by date and time
        from :model:`makeover.Booking`
    ``booking_form``
        An instance of :form:`makeover.BookingForm` for submitting booking requests.

     **Template**
        :template:`makeover/makeover.html`
    """
    makeover = Makeover.objects.all().order_by("-updated_on").first()

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            bookings = booking_form.save(commit=False)
            bookings.username = request.user
            bookings.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Booking submitted! It will appear faded until confirmed. Phone us if you would like a short-notice appointment.",
            )

    else:
        booking_form = BookingForm()

    bookings = (
        Booking.objects.all()
        .filter(username=request.user)
        .order_by("date_of_booking", "start_time")
    )

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
    """
    Edit a booking

    Uses :model: `booking.Booking`

    **Context**

    ``booking``
        represents the booking instance to be edited

     **Template**

    :template:`makeover/edit_makeover.html`

    """

    model = Booking
    template_name = "makeover/edit_makeover.html"
    form_class = BookingForm
    success_url = "/makeover/"

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
        return self.request.user == booking.username or self.request.user.is_superuser


# Credit: https://www.youtube.com/watch?v=JzDBCZTgVyw&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=14
# Credit: https://github.com/Dee-McG/Recipe-Tutorial/blob/main/recipes/views.py#L72
# Credit: https://github.com/DanMorriss/nialls-barbershop/blob/main/booking_system/views.py#L272
# Customised: using the form valid function here
class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Displays a new page to confirm deletion of a booking

    Uses :model: `booking.Booking`

    **Context**

    ``booking``
        Represents the booking instance to be deleted. Comes from :model:`makeover.Booking`

    **Template**

    :template:`blog/comment_confirm_delete.html`

    Redirects to success url which is "/makeover/"
    """

    model = Booking
    success_url = "/makeover/"

    def form_valid(self, form):
        messages.success(
            self.request,
            "Your booking has been deleted successfully!",
            extra_tags="alert alert-success alert-dismissible",
        )

        return super().form_valid(form)

    # Credit: https://github.com/DanMorriss/nialls-barbershop/blob/main/booking_system/views.py#L312
    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.username or self.request.user.is_superuser
