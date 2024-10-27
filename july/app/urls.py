from django.urls import path
from app import views
urlpatterns=[
    path("nanda",views.nanda,name="nandapage"),
    path('home',views.home,name="homepage"),
    path('contact',views.contact,name="contactpage"),
    path('help',views.help,name="helppage"),
    path('about',views.about,name="aboutpage"),
    path('palind/<str:s>',views.palind,name="palindromea"),
    path('redirect',views.redrect,name="redirecttpage")
    

] 