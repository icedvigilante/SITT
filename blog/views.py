from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import BlogPost, Category
from .forms import PostForm, PostEditForm, CategoryAddForm, CategoryEditForm


class BlogView(ListView):
    model = BlogPost
    template_name = 'blog/home.html'
    ordering = ['-pk']

    def form_valid(self, form):
        form.instance.author = self.request.user.id
        return super().form_valid(form)


class BlogAddView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = PostForm
    # fields = ('title',
    #           'header_image',
    #           'snippet',
    #           'category',
    #           'body')
    template_name = 'blog/post_add.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'


class BlogEditView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    form_class = PostEditForm
    template_name = 'blog/post_edit.html'


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog:home')


class CategoryAddView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryAddForm
    template_name = "blog/category_add.html"
    success_url = reverse_lazy('blog:category_list')


class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category.html'


class CategoryEditView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryEditForm
    template_name = 'blog/category_edit.html'


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'blog/category_delete.html'
    success_url = reverse_lazy('blog:category_list')
