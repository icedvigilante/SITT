from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = 'mainsite/home.html'


class OriginScriptsView(TemplateView):
    template_name = 'mainsite/origin_scripts.html'


class UserEnvScriptsView(TemplateView):
    template_name = 'mainsite/user_env_script.html'
