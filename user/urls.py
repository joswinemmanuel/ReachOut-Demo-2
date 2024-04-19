from django.urls import path
from . import views

urlpatterns = [
    path("journaling/", views.journaling, name="journaling"),
    path("appointments/", views.appointments, name="appointments"),
    path("chatbot/", views.chatbot, name="chatbot"),
    path("recommended/", views.recommended, name="recommended"),
    path("dailytask/", views.dailytask, name="dailytask"),
    path("progress/", views.progress, name="progress"),
    path("dashboard/", views.dashboard, name="dashboard"),
]