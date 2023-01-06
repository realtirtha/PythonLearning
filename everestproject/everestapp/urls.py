from django.urls import path
from .views import *

app_name = "everestapp"

urlpatterns =[
    path("", ClientHomeView.as_view(), name = "clienthome"),
    path("about/",ClientAboutView.as_view(),name="clientabout"),
    path("news/",ClientNewsView.as_view(),name="clientnews"),
    path("news/<int:pk>/",ClientNewsDetailView.as_view(), name="clientnewsdetail"),

    path("news/create/",ClientNewsCreateView.as_view(), name="clientnewscreate"),
]