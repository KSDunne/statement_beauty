from . import views
from django.urls import path

urlpatterns = [
    path('', views.makeover_deals, name='makeover'),
]