from django.views.generic import View, TemplateView, ListView, DetailView
from .models import *

# Create your views here.

class ClientHomeView(TemplateView):  
    template_name = "clienthome.html"

class ClientAboutView(ListView):
    template_name = "clientabout.html"
    model = Category
    context_object_name ='categories'

class ClientNewsView(ListView):
    template_name = "clientnews.html"
    model = News
    context_object_name='news'

class ClientNewsDetailView(DetailView):
    template_name = "clientnewsdetail.html"
    model = News
    context_object_name='newsdetail'