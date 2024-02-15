from django.shortcuts import render
from .models import Makeover


def makeover_deals(request):
    """
    Renders the Makeover page
    """
    makeover = Makeover.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "makeover/makeover.html",
        {"makeover": makeover},
    )