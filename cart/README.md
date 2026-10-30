# E-Commerce Backend (Django)

A full-featured e-commerce backend built with Django.

## Features

- Product listing and product detail pages
- Category filtering
- Product search
- Shopping cart (add, update, remove)
- User authentication (signup, login, logout)
- Checkout and order placement
- Order history for logged-in users
- Automatic stock reduction after order
- Django admin panel

## Tech Stack

- Python
- Django
- SQLite (development)
- Bootstrap (UI)

## Project Structure

- `store` : products, categories, search
- `cart` : session-based shopping cart
- `orders` : checkout and order management
- `accounts` : authentication
- `config` : project settings

## How to Run

```bash
# clone the project
git clone https://github.com/maunta91/ecommerce-backend-django.git
cd ecommerce-backend-django

# create virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# install dependencies
pip install django pillow

# run migrations
python manage.py migrate

# create admin user
python manage.py createsuperuser

# run server
python manage.py runserver

//then open: http://127.0.0.1:8000/
Admin panel:
http://127.0.0.1:8000/admin/

//What I Learned
Django MVT architecture
Models, views, templates, and URL routing
Session-based cart system
User authentication and permissions
Order processing and stock management
Git and branch workflow

//Future Improvements
Payment gateway integration
Product image gallery
REST API with Django REST Framework
Deployment to cloud