from django.urls import path, include
from .import views
urlpatterns=[
    path('',views.home ,name='home'),
    path('about/',views.about, name='about'),
    path('rooms/',views.rooms, name='rooms'),
    path('booking/',views.booking, name='booking'),
    path('contactus/',views.contactus,name='contactus'),
]