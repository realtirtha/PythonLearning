from django.urls import path
from .views import *

app_name = "initapp"

urlpatterns = [
    path("",IndexView.as_view(),name="index"),
    path("/about/",AboutView.as_view(),name="about")
]

