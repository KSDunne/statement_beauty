from django.urls import path
from . import views

urlpatterns = [
    path('', views.makeover_deals, name='makeover'),
    path('booking_edit/<int:booking_id>', views.booking_edit, name='booking_edit'),
    path('delete_booking/<int:booking_id>', views.delete_booking, name='delete_booking'),
]