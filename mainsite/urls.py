from django.urls import path
from .views import IndexView, OriginScriptsView, UserEnvScriptsView

app_name = 'mainsite'
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('origin_scripts', OriginScriptsView.as_view(), name='origin_scripts'),
    path('user_env_script', UserEnvScriptsView.as_view(), name='user_env_script'),
]
