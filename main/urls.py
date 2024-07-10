from django.urls import path

import main.views
from . import views
from learning import views

urlpatterns = [
    path('', main.views.index),
    path('about', main.views.about),
    path('hoho', views.hoho),
    path('img', views.page),

]
