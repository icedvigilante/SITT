from django.urls import path
from .views import BlogView, AddBlogView

app_name = 'blog'
urlpatterns = [
    path('', BlogView.as_view(), name='home'),
    path('add/', AddBlogView.as_view(), name='add'),
]