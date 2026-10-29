import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods

from .models import Booking


def book(request):
    # TODO: Render the booking page and handle valid POST submissions.
    # Validate required fields and reject duplicate date/time slots.
    return render(request, "restaurant/book.html")


@require_GET
def reservations(request):
    # TODO: Return all reservations as JSON.
    # Consider returning a list of objects with first_name,
    # reservation_date, and reservation_slot.
    return JsonResponse({"detail": "TODO: implement reservations JSON"}, status=501)


@require_GET
def bookings_by_date(request):
    # TODO: Read ?date=YYYY-MM-DD, validate it, and return matching bookings.
    # If there are no matches, the frontend should display "No Booking".
    return JsonResponse({"detail": "TODO: implement date-filtered bookings"}, status=501)
