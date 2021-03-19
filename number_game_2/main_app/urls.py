from django.urls import path
from . import views
urlpatterns= [

    path('', views.index),
    path('replay', views.replay),
    path('clear', views.clear),
]