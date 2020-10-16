from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import BlogPost, Category
from .forms import PostForm, EditPostForm, AddCategoryForm, EditCategoryForm
from django.urls import reverse_lazy, reverse


class BlogView(ListView):
    model = BlogPost
    template_name = 'blog_home.html'
    ordering = ['-post_date']

    def form_valid(self, form):
        form.instance.author = self.request.user.id
        return super().form_valid(form)

    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.ordering.all()
    #     context = super(BlogView, self).get_context_data(*args, **kwargs)
    #     context['cat_menu'] = cat_menu
    #     return context

# def BlogView(request):
#     return render(request, 'blog_home.html', {})

class AddBlogView(CreateView):
    model = BlogPost
    form_class = PostForm
    template_name = 'add_post.html'

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'


class EditBlogPostView(UpdateView):
    model = BlogPost
    form_class = EditPostForm
    template_name = 'edit_post.html'


class DeleteBlogPostView(DeleteView):
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog_home')


class AddCategoryView(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = "add_category.html"


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'


class EditCategoryView(UpdateView):
    model = Category
    form_class = EditCategoryForm
    template_name = 'edit_category.html'


class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'delete_category.html'
    success_url = reverse_lazy('category_list')