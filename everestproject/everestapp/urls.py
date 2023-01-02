from django.urls import path
from .views import *

app_name = "everestapp"

urlpatterns =[
    path("", ClientHomeView.as_view(), name = "clienthome"),
]