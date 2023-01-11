from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(TemplateView):
    template_name = "contact.html"