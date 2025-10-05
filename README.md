# 🧋 Milk Tea Online Ordering and Payment System

A Django-based web application that follows the exact flow from the provided flowchart for ordering milk tea online.

## 📋 Features

Following the flowchart flow:
1. **Enter the system** - Welcome page with system overview
2. **Browse the menu** - View available drinks, flavors, and toppings
3. **Decide an order** - Customize drinks with specific add-ons
4. **Proceed to the counter** - Review order summary
5. **Place the order** - Confirm order details
6. **Process Payment** - Choose between cash or credit card
7. **Wait for the drink** - Real-time order status tracking
8. **Receive the drink** - Order pickup confirmation
9. **Enjoy the drink** - Order completion and feedback
10. **Exit the website** - Thank you page

## 🛠 Tech Stack

- **Backend**: Django (Python)
- **Frontend**: Vanilla HTML, CSS, JavaScript
- **Database**: SQLite (default Django)
- **Styling**: Custom CSS with responsive design

## 📁 Project Structure

```
src/
├── manage.py
├── milk_tea_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── ordering/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── templates/
│   ├── base.html
│   └── ordering/
│       ├── enter_system.html
│       ├── browse_menu.html
│       ├── proceed_to_counter.html
│       ├── process_payment.html
│       ├── wait_for_drink.html
│       ├── receive_drink.html
│       ├── enjoy_drink.html
│       └── exit_website.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── main.js
```

## 🚀 Setup Instructions

1. **Install Python** (3.8 or higher)

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to src directory**:
   ```bash
   cd src
   ```

5. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

7. **Load sample data** (optional):
   ```bash
   python manage.py shell
   ```
   Then run:
   ```python
   from ordering.models import Drink, Flavor, Topping, Size
   
   # Create sizes
   Size.objects.create(name="Small", price_multiplier=0.8)
   Size.objects.create(name="Medium", price_multiplier=1.0)
   Size.objects.create(name="Large", price_multiplier=1.3)
   
   # Create flavors
   Flavor.objects.create(name="Original", additional_price=0.00)
   Flavor.objects.create(name="Taro", additional_price=0.50)
   Flavor.objects.create(name="Matcha", additional_price=0.50)
   Flavor.objects.create(name="Chocolate", additional_price=0.50)
   
   # Create toppings
   Topping.objects.create(name="Pearls", price=0.75)
   Topping.objects.create(name="Jelly", price=0.50)
   Topping.objects.create(name="Pudding", price=0.60)
   Topping.objects.create(name="Red Bean", price=0.65)
   
   # Create drinks
   Drink.objects.create(name="Classic Milk Tea", base_price=4.50, description="Traditional milk tea with black tea base")
   Drink.objects.create(name="Thai Milk Tea", base_price=5.00, description="Sweet and creamy Thai-style milk tea")
   Drink.objects.create(name="Brown Sugar Milk Tea", base_price=5.50, description="Rich brown sugar syrup with fresh milk")
   Drink.objects.create(name="Fruit Tea", base_price=4.00, description="Refreshing fruit-infused tea")
   ```

8. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

9. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000`

## 🎯 Usage

1. **Start**: Visit the homepage and click "Enter System & Browse Menu"
2. **Browse**: View available drinks and their customization options
3. **Order**: Select drinks, sizes, flavors, and toppings, then add to order
4. **Review**: Proceed to counter to review your order summary
5. **Place**: Confirm your order to proceed to payment
6. **Pay**: Choose cash or credit card payment method
7. **Track**: Wait for your drink with real-time status updates
8. **Pickup**: Receive your drink when ready
9. **Complete**: Enjoy your drink and provide feedback
10. **Exit**: Thank you page with option to order again

## 🔧 Models

- **Drink**: Base milk tea products
- **Flavor**: Available flavor options
- **Topping**: Add-on toppings (pearls, jelly, pudding)
- **Size**: Drink sizes with price multipliers
- **Order**: Customer orders with status tracking
- **OrderItem**: Individual items within an order
- **Payment**: Payment records with method and status

## 🎨 Features

- **Dynamic Pricing**: Real-time price calculation based on selections
- **Order Tracking**: Live status updates from placed to ready
- **Responsive Design**: Works on desktop and mobile devices
- **Session Management**: Cart persistence during browsing
- **Admin Interface**: Django admin for managing products and orders
- **AJAX Updates**: Smooth status updates without page refresh

## 🔄 Order Status Flow

1. **Pending** → **Placed** → **Preparing** → **Ready** → **Completed**

## 📱 API Endpoints

- `GET /api/order-status/<order_number>/` - Get current order status
- `POST /api/update-status/<order_number>/` - Update order status (admin)

## 🎭 Demo Features

- Auto-progression of order status for demonstration
- Simulated payment processing
- Interactive rating system
- Animated UI elements

## 🚀 Deployment

For production deployment:
1. Set `DEBUG = False` in settings.py
2. Configure proper database (PostgreSQL recommended)
3. Set up static file serving
4. Configure allowed hosts
5. Use environment variables for sensitive settings

## 📄 License

This project is created for educational purposes following the provided flowchart specifications.
