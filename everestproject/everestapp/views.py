from django.views.generic import View, TemplateView

# Create your views here.

class ClientHomeView(TemplateView):
    template_name = "clienthome.html"