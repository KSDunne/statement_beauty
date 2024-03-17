from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """

    summernote_fields = ("content",)


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """

    list_display = (
        "message",
        "read",
    )
