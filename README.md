# Adel-s-restaurant
# Adel's Restaurant Booking System

A comprehensive restaurant booking system built with Django that allows users to make table reservations and view the restaurant's menu.

## Features

- **User Authentication**: Register, login, and manage user profiles
- **Booking System**: Create, view, update, and cancel table reservations
- **Menu Display**: Browse restaurant menu by categories
- **Admin Panel**: Manage tables, bookings, and menu items
- **Responsive Design**: Works on desktop and mobile devices

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: PostgreSQL (production) / SQLite (development)
- **Deployment**: Heroku
- **Version Control**: Git, GitHub

## Installation

### Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)
- PostgreSQL or MySQL (optional for development)

### Setup

1. Clone the repository
git clone https://github.com/suadtech/adels-restaurant.git
cd adels-restaurant

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Set up environment variables
Create a `.env` file in the project root with the following variables:
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3  # For development

5. Run migrations
python manage.py migrate

6. Create a superuser
python manage.py createsuperuser

7. Load sample menu data (optional) 
python create_sample_menu.py

8. Run the development server
python manage.py runserver

9. Access the site at http://127.0.0.1:8000/

## Usage

### Making a Reservation
1. Register or log in to your account
2. Navigate to "Book a Table"
3. Select date, time, and number of guests
4. Submit your booking

### Viewing/Modifying Reservations
1. Log in to your account
2. Go to "My Bookings"
3. View, edit, or cancel your reservations

### Browsing the Menu
1. Navigate to "Menu"
2. Browse by category
3. Click on items to view details

## Deployment

The application is configured for deployment on Heroku:

1. Create a Heroku app
heroku create adels-restaurant

2. Add PostgreSQL add-on
heroku addons:create heroku-postgresql:hobby-dev

3. Configure environment variables on Heroku
heroku config:set SECRET_KEY=your_secret_key
heroku config:set DEBUG=False

4. Deploy to Heroku
git push heroku main

5. Run migrations on Heroku
heroku run python manage.py migrate

6. Create superuser on Heroku
heroku run python manage.py createsuperuser

## Project Structure

adels_restaurant/
├── accounts/            # User authentication app
├── booking/             # Booking management app
├── menu/                # Menu display app
├── adels_restaurant_project/  # Project settings
├── static/              # Static files (CSS, JS, images)
├── templates/           # HTML templates
├── media/               # User-uploaded files
├── requirements.txt     # Project dependencies
├── Procfile             # Heroku deployment configuration
├── runtime.txt          # Python version for Heroku
└── README.md            # Project documentation

## Credits and Attribution

- Bootstrap framework: https://getbootstrap.com/
- Django framework: https://www.djangoproject.com/
- Font Awesome icons: https://fontawesome.com/

## License

This project is licensed under the MIT License - see the LICENSE file for details.
