# Little Lemon booking project starter

This is a **starter scaffold**, not a completed assessment submission. Use it to build and test your own implementation against the course rubric.

## Setup
1. Install Python and MySQL.
2. Install Pipenv if needed: `pip install pipenv`
3. From this folder run:
   ```bash
   pipenv install
   pipenv shell
   ```
4. Create a MySQL database, then update `DATABASES` in `littlelemon/settings.py`.
5. Run:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

## Complete these TODOs
- Configure your local MySQL database credentials in `littlelemon/settings.py`.
- Implement booking validation and duplicate-slot prevention in `restaurant/views.py`.
- Complete the reservation JSON endpoint and date filtering.
- Finish the JavaScript Fetch API behavior in `restaurant/static/restaurant/js/booking.js`.
- Test all 13 peer-review criteria using your own local project.

Never commit real database passwords or secret keys.
