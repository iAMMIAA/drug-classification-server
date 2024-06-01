from django.urls import path
from . import views

urlpatterns = [
    #API Drug
    path('classify_drug/', views.classify_drug, name = 'url_img'),
]
