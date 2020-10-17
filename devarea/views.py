from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import DevPost
from .forms import DevForm


class HomeView(ListView):
    model = DevPost
    template_name = "devarea/home.html"
    ordering = ['post_date']

    def form_valid(self, form):
        form.instance.author = self.request.user.id
        return super().form_valid(form)


class DevAddView(LoginRequiredMixin, CreateView):
    model = DevPost
    form_class = DevForm
    template_name = 'devarea/dev_add.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DevDetailView(DetailView):
    model = DevPost
    template_name = 'devarea/dev_detail.html'


class DevEditView(LoginRequiredMixin, UpdateView):
    model = DevPost
    form_class = DevForm
    template_name = 'devarea/dev_edit.html'


class DevDeleteView(LoginRequiredMixin, DeleteView):
    model = DevPost
    template_name = 'devarea/dev_delete.html'
    success_url = reverse_lazy('devarea:home')
