from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import BlogPost
from .forms import PostForm, EditPostForm


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


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'


class EditBlogPostView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    form_class = EditPostForm
    template_name = 'blog/edit_post.html'


class DeleteBlogPostView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:home')


# class AddCategoryView(LoginRequiredMixin, CreateView):
#     model = Category
#     form_class = AddCategoryForm
#     template_name = "blog/add_category.html"
