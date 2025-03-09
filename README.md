# E-Commerce Platform (Built with Python & Django)

An e-commerce platform built using **Python** and **Django** that allows users to browse products, add them to a cart, and complete purchases. This project provides essential e-commerce functionalities such as user authentication, order management, and payment processing.

## Features
- **Built with Django (Python Web Framework)**
- User authentication (signup, login, logout)
- Product listing with categories
- Shopping cart functionality
- Order placement and tracking
- Payment gateway integration (if applicable)
- Admin dashboard for managing products and orders

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default) / MySQL (optional)
- **Authentication**: Django Authentication System

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/ShahWalig/ecommerce.git
   ```
2. Navigate to the project directory:
   ```sh
   cd ecommerce
   ```
3. Create and activate a virtual environment:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Apply migrations:
   ```sh
   python manage.py migrate
   ```
6. Create a superuser (optional, for admin access):
   ```sh
   python manage.py createsuperuser
   ```
7. Run the project:
   ```sh
   python manage.py runserver
   ```

## Usage
- Open `http://127.0.0.1:8000/` in your browser.
- Register or log in to start shopping.
- Browse products and add them to your cart.
- Proceed to checkout and place your order.

## Contributing
If you'd like to contribute, feel free to fork the repository and create a pull request.

## License
This project is open-source and available under the MIT License.

## Contact
For any questions or support, reach out via email: `shahwaliweb@gmail.com`
