from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
