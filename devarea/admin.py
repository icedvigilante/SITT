from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import DevPost


class DevPostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(DevPost, DevPostAdmin),