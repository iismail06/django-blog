from django.contrib import admin
from .models import About  # Import the About model
from django_summernote.admin import SummernoteModelAdmin  # Import SummernoteModelAdmin


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
   

  