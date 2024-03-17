from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    A form for creating collaboration requests
    """

    class Meta:
        """
        Uses :model:`about.CollaborationRequest`. This form
        collects information from users who want to collaborate.
        It includes fields for the user's name, email, their area of
        interest for collaboration and a message.
        """

        model = CollaborateRequest
        fields = ("name", "email", "interest", "message")
