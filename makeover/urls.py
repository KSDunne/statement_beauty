from . import views
from django.urls import path

urlpatterns = [
    path('', views.makeover_deals, name='makeover'),
    path('booking_edit/<int:booking_id>/',
         views.booking_edit, name='booking_edit'),
]