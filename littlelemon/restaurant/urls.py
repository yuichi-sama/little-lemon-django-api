from django.urls import path
from . import views

app_name = "restaurant"

urlpatterns = [
    path("book/", views.book, name="book"),
    path("reservations/", views.reservations, name="reservations"),
    path("bookings", views.bookings_by_date, name="bookings-by-date"),
]
