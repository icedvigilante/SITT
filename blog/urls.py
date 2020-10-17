from django.urls import path
from .views import BlogView, AddBlogView, AddCategoryView, BlogDetailView, EditBlogPostView, DeleteBlogPostView

app_name = 'blog'
urlpatterns = [
    path('', BlogView.as_view(), name='home'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('edit/<int:pk>/', EditBlogPostView.as_view(), name='blog_edit'),
    path('delete/<int:pk>/', DeleteBlogPostView.as_view(), name='blog_delete'),
    path('blog_add/', AddBlogView.as_view(), name='blog_add'),
    path('category_add/', AddCategoryView.as_view(), name='category_add'),
]