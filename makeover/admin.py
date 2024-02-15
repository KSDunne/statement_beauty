from django.contrib import admin
from .models import Makeover
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Makeover)
class MakeoverAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

