from django.urls import path
from .views import HomeView, DevAddView, DevDetailView, DevEditView, DevDeleteView

app_name = 'devarea'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dev_add/', DevAddView.as_view(), name='app_add'),
    path('<int:pk>/', DevDetailView.as_view(), name='app'),
    path('edit/<int:pk>', DevEditView.as_view(), name='dev_edit'),
    path('delete/<int:pk>', DevDeleteView.as_view(), name='dev_delete'),
]