from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("site1_printing/", views.SiteOneHome, name="printing"),
    path("site2_instruments/", views.SiteTwoHome, name="instruments"),
]
