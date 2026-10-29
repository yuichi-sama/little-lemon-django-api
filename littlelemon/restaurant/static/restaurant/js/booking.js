// TODO: Complete the booking-form behavior using Fetch API.
// Required behavior from the rubric:
// 1. Select today's date by default.
// 2. Fetch bookings for the selected date.
// 3. Refresh the displayed bookings when the date changes.
// 4. Disable already-booked time slots.
// 5. Handle empty results by displaying "No Booking".
// 6. Handle failed requests and invalid form submissions clearly.

document.addEventListener("DOMContentLoaded", () => {
  const dateInput = document.getElementById("reservation_date");
  const slotSelect = document.getElementById("reservation_slot");
  const bookingList = document.getElementById("booking-list");
  const noBooking = document.getElementById("no-booking");

  // TODO: Set dateInput.value to today's date in YYYY-MM-DD format.
  // TODO: Implement a function that fetches `/bookings?date=YYYY-MM-DD`.
  // TODO: Render the response and disable booked options in slotSelect.
  // TODO: Call the function on initial load and on dateInput change.
});
