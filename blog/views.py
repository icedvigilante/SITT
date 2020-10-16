from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import BlogPost, Category
from .forms import PostForm, AddCategoryForm


class BlogView(ListView):
    model = BlogPost
    template_name = 'blog/home.html'
    ordering = ['-post_date']

    def form_valid(self, form):
        form.instance.author = self.request.user.id
        return super().form_valid(form)


class AddBlogView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = PostForm
    # fields = ('title',
    #           'header_image',
    #           'snippet',
    #           'category',
    #           'body')
    template_name = 'blog/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCategoryView(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = "add_category.html"
