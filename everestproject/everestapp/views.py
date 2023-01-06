from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
from .models import *
from .forms import *
from django.urls import reverse, reverse_lazy

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

class ClientNewsCreateView(CreateView):
    template_name = "clientnewscreate.html"
    form_class = ClientNewsCreateForm
    model = News
    success_url = reverse_lazy("everestapp:clienthome")