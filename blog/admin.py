from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost, Category


class BlogPostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(BlogPost, BlogPostAdmin),
admin.site.register(Category),
