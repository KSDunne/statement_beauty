from django.urls import path
from . import views
from .views import EditBooking

urlpatterns = [
    path('', views.makeover_deals, name='makeover'),
    path('booking_edit/<int:pk>/', EditBooking.as_view(), name='edit_booking'),
    path('delete_booking/<int:booking_id>', views.delete_booking, name='delete_booking'),
]