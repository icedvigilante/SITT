from django.shortcuts import render
from django.views.generic import ListView
from .models import DevPost


class HomeView(ListView):
    model = DevPost
    template_name = "devarea/home.html"

    def form_valid(self, form):
        form.instance.author = self.request.user.id
        return super().form_valid(form)
