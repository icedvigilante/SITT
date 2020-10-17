from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from accounts.models import CustomUser
from django.contrib.auth.models import Group
from django.urls import reverse


class DevPost(models.Model):
    app_name = models.CharField(max_length=150)
    app_type = models.CharField(max_length=150)
    screenshot = models.ImageField(null=True, blank=True, upload_to='images/dev/screenshots')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    snippet = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField(blank=True, null=True)
    git_hub = models.URLField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.app_name + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('devrea:home')
