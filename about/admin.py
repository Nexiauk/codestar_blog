from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(About)

# customising admin page for faster searches, filters and headers
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')