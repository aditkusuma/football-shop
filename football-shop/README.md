# Football Shop Project

## Overview
The Football Shop project is a web application built using Django that allows users to manage football-related products. It implements CRUD (Create, Read, Update, Delete) operations for products and provides user authentication functionalities through AJAX.

## Features
- User registration and login using AJAX.
- Create, read, update, and delete products using AJAX.
- Responsive design with a user-friendly interface.
- Toast notifications for user feedback.

## Project Structure
```
football-shop/
├── main/
│   ├── migrations/          # Database migration files
│   ├── __init__.py
│   ├── models.py            # Data models for the application
│   ├── views.py             # View functions for handling requests
│   ├── forms.py             # Forms for product and user management
│   ├── urls.py              # URL routing for the application
│   ├── templates/           # HTML templates for rendering views
│   │   ├── base.html
│   │   ├── main.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── modal.html
│   │   ├── navbar.html
│   │   └── toast.html
│   └── static/              # Static files (CSS, JS)
│       └── css/
│           └── global.css
├── football_shop/
│   ├── __init__.py
│   ├── settings.py          # Project settings and configuration
│   ├── urls.py              # Root URL routing
│   └── wsgi.py              # WSGI application for deployment
├── manage.py                 # Command-line utility for managing the project
└── README.md                 # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd football-shop
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage
- Navigate to `http://127.0.0.1:8000/` in your web browser.
- Register a new account or log in with an existing account.
- Manage products by creating, viewing, editing, or deleting them.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.