from django.views.generic import View, TemplateView, ListView
from .models import *

# Create your views here.

class ClientHomeView(TemplateView): 
    template_name = "clienthome.html"

class ClientAboutView(ListView):
    template_name = "clientabout.html"
    model = Category
    context_object_name ='categories'