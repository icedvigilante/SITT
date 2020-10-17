from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from accounts.models import CustomUser
from django.contrib.auth.models import Group
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:home')


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    snippet = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('blog:home')
