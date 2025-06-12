from django.urls import path
from . import views

urlpatterns = [
    path("meetings/", views.MeetingListCreate.as_view(), name="meeting-list-create"),
    path("meetings/delete/<int:pk>/", views.MeetingDelete.as_view(), name="meeting-delete"),
]