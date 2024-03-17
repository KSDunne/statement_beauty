from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from datetime import datetime, date
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ("date_of_booking", "service_type", "start_time", "message")
        widgets = {
            "date_of_booking": DateInput(attrs={"type": "date"}),
        }

        labels = {
            "date_of_booking": "Date",
            "service_name": "Service",
            "start_time": "Time",
            "message": "Message",
        }

    def clean(self):
        cleaned_data = super().clean()
        date_of_booking = cleaned_data.get("date_of_booking")
        start_time = cleaned_data.get("start_time")

        if date_of_booking < date.today():
            raise ValidationError("Please select a date in the future.")

        if (date_of_booking ==
                date.today() and start_time < datetime.now().time()):
            raise ValidationError("Please select a time in the future.")

        existing_bookings = Booking.objects.filter(
            date_of_booking=date_of_booking, start_time=start_time
        ).exclude(id=self.instance.id)

        if existing_bookings:
            raise ValidationError(
                "That time is already taken, "
                "please select a different time."
            )
