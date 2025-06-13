from django.urls import path
from . import views

urlpatterns = [
    path("google/login/", views.GoogleLogin.as_view(), name="google-login"),
    path("meetings/", views.MeetingListCreate.as_view(), name="meeting-list-create"),
    path("meetings/delete/<int:pk>/", views.MeetingDelete.as_view(), name="meeting-delete"),
]