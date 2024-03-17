from django.db import models
from django.contrib.auth.models import User
import datetime

BOOKING_TIME = (
    (datetime.time(8, 30, 0), "8:30am"),
    (datetime.time(9, 0, 0), "9:00am"),
    (datetime.time(9, 30, 0), "9:30am"),
    (datetime.time(10, 0, 0), "10:00am"),
    (datetime.time(10, 30, 0), "10:30am"),
    (datetime.time(11, 0, 0), "11:00am"),
    (datetime.time(11, 30, 0), "11:30am"),
    (datetime.time(12, 0, 0), "12:00pm"),
    (datetime.time(12, 30, 0), "12:30pm"),
    (datetime.time(13, 0, 0), "1:00pm"),
    (datetime.time(13, 30, 0), "1:30pm"),
    (datetime.time(14, 0, 0), "2:00pm"),
    (datetime.time(14, 30, 0), "2:30pm"),
    (datetime.time(15, 0, 0), "3:00pm"),
    (datetime.time(15, 30, 0), "3:30pm"),
    (datetime.time(16, 0, 0), "4:00pm"),
    (datetime.time(16, 30, 0), "4:30pm"),
)

SERVICE = (("Makeup Appointment", "Makeup"), ("Hair Appointment", "Hair"))


class Makeover(models.Model):
    """
    Model for displaying the makeover deal of the season.

    Fields:
        - `title` (CharField): A heading for the deal of the season
        - `updated_on` (DateTimeField): Date the last deal was updated on the
        website so customer knows if the deal was added a long time ago,
        it may be expired.
        - `content` (TextField): A text field for a description of the deal
        of the season
    """

    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class Booking(models.Model):
    """
    Model for bookings with username related to :model:`auth.User`.

    Fields:
        - `username` (ForeignKey): Reference to the user making the booking.
        - `date_of_booking` (DateField): Date of the reservation.
        - `service_type` (IntegerField): Reference to the booked service.
        - `start_time` (TimeField): Start time of the reservation chosen from
        predefined choices.
        - `confirmed` (BooleanField): Indicates whether the booking is
        confirmed.
        - `message` (CharField): A free text area to allow the customer to
        make addition comments or ask a question.

    Meta:
        - `ordering`: Default ordering for queries based on date and
        start time.

    Methods:
        - `__str__`: Human-readable string representation of the booking.
    """

    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="username_booking"
    )
    date_of_booking = models.DateField()
    service_type = models.TextField(choices=SERVICE)
    start_time = models.TimeField(choices=BOOKING_TIME)
    confirmed = models.BooleanField(default=False)
    message = models.TextField(max_length=500)

    class Meta:
        ordering = ["date_of_booking", "start_time"]

    def __str__(self):
        return (
            f"{self.service_type} for {self.username} "
            f"on {self.date_of_booking} at {self.start_time}"
        )
