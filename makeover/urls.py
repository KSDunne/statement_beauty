from django.urls import path
from . import views
from .views import EditBooking, DeleteBooking

urlpatterns = [
    path('', views.makeover_deals, name='makeover'),
    path('booking_edit/<int:pk>/', EditBooking.as_view(), name='edit_booking'),
    path('delete_booking/<int:pk>', DeleteBooking.as_view(), name='delete_booking'),
]