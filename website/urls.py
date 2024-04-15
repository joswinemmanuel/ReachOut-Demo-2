from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("assistance/", views.assistance, name="assistance"),
    path("contact/", views.contact, name="contact"),
    path("team/", views.team, name="team"),
    path("testimonial/", views.testimonial, name="testimonial"),
    path("404/", views.Error404, name="404"),
    path("login/", views.user_login, name="user_login"),
]