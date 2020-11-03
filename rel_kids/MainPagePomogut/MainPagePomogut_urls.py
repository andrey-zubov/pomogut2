from django.conf.urls import  url, include
from . import views

urlpatterns = [
    url(r'^$', views.hello),
    url(r'add_the_information_about_us/', views.add_the_information_about_us),
]