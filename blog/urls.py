from django.urls import path
from .views import BlogView, BlogAddView, BlogDetailView, BlogEditView, BlogDeleteView, CategoryAddView,\
    CategoryListView, CategoryEditView, CategoryDeleteView

app_name = 'blog'
urlpatterns = [
    path('', BlogView.as_view(), name='home'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('edit/<int:pk>/', BlogEditView.as_view(), name='blog_edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog_add/', BlogAddView.as_view(), name='blog_add'),
    path('category/', CategoryListView.as_view(), name="category_list"),
    path('category_add/', CategoryAddView.as_view(), name='category_add'),
    path('category_edit/<int:pk>', CategoryEditView.as_view(), name="category_edit"),
    path('category_delete/<int:pk>', CategoryDeleteView.as_view(), name="category_delete"),
]
