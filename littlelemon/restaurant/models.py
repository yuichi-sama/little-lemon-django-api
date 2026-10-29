from django.db import models

class Booking(models.Model):
    # TODO: Add the three fields required by the rubric:
    # first_name, reservation_date, reservation_slot.
    # Choose field types and constraints appropriate to your implementation.
    pass

    def __str__(self):
        return f"Booking #{self.pk}"
