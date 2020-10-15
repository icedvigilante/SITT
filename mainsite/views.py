from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = 'home.html'


class OriginScriptsView(TemplateView):
    template_name = 'origin_scripts.html'


class UserEnvScriptsView(TemplateView):
    template_name = 'user_env_script.html'
