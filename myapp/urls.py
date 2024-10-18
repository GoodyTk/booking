from django.urls import path, include
from django.contrib import admin
from myapp import views

urlpatterns = [
    path("rooms/", views.room_list, name="room-list"),
    path("book-room/", views.booking_room, name="book-room"),
    path("booking-details/<int:pk>", views.booking_details, name="booking-details"),
    path("", views.home_page, name="home-page")
]
