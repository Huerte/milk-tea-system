"""
Populate database with realistic milk tea products and options
Run this script with: python manage.py shell < populate_data.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'milk_tea_system.settings')
django.setup()

from ordering.models import Drink, Flavor, Topping, Size


print("Clearing existing data...")
Drink.objects.all().delete()
Flavor.objects.all().delete()
Topping.objects.all().delete()
Size.objects.all().delete()


print("\nCreating sizes...")
sizes_data = [
    {"name": "Small (12oz)", "price_multiplier": 0.85},
    {"name": "Medium (16oz)", "price_multiplier": 1.00},
    {"name": "Large (20oz)", "price_multiplier": 1.25},
]

for size_data in sizes_data:
    size = Size.objects.create(**size_data)
    print(f"  ✓ Created size: {size.name}")


print("\nCreating flavors...")
flavors_data = [
    {"name": "Original", "additional_price": 0.00},
    {"name": "Taro", "additional_price": 0.50},
    {"name": "Matcha", "additional_price": 0.60},
    {"name": "Chocolate", "additional_price": 0.50},
    {"name": "Strawberry", "additional_price": 0.50},
    {"name": "Mango", "additional_price": 0.60},
    {"name": "Honeydew", "additional_price": 0.50},
    {"name": "Lavender", "additional_price": 0.70},
]

for flavor_data in flavors_data:
    flavor = Flavor.objects.create(**flavor_data)
    print(f"  ✓ Created flavor: {flavor.name} (+${flavor.additional_price})")


print("\nCreating toppings...")
toppings_data = [
    {"name": "Tapioca Pearls", "price": 0.75},
    {"name": "Crystal Boba", "price": 0.80},
    {"name": "Grass Jelly", "price": 0.60},
    {"name": "Aloe Vera", "price": 0.65},
    {"name": "Pudding", "price": 0.70},
    {"name": "Red Bean", "price": 0.75},
    {"name": "Coconut Jelly", "price": 0.65},
    {"name": "Popping Boba", "price": 0.85},
    {"name": "Cheese Foam", "price": 1.00},
]

for topping_data in toppings_data:
    topping = Topping.objects.create(**topping_data)
    print(f"  ✓ Created topping: {topping.name} (+${topping.price})")


print("\nCreating drinks...")
drinks_data = [
    {
        "name": "Classic Milk Tea",
        "base_price": 4.50,
        "description": "Traditional black tea with creamy milk, a timeless favorite",
        "is_available": True
    },
    {
        "name": "Brown Sugar Boba Milk",
        "base_price": 5.50,
        "description": "Fresh milk with rich brown sugar syrup and chewy tapioca pearls",
        "is_available": True
    },
    {
        "name": "Thai Milk Tea",
        "base_price": 5.00,
        "description": "Authentic Thai tea with condensed milk, sweet and aromatic",
        "is_available": True
    },
    {
        "name": "Taro Milk Tea",
        "base_price": 5.25,
        "description": "Creamy taro blended with milk, naturally sweet and purple",
        "is_available": True
    },
    {
        "name": "Matcha Latte",
        "base_price": 5.75,
        "description": "Premium Japanese matcha powder with steamed milk",
        "is_available": True
    },
    {
        "name": "Jasmine Green Tea",
        "base_price": 4.00,
        "description": "Fragrant jasmine green tea, light and refreshing",
        "is_available": True
    },
    {
        "name": "Passion Fruit Tea",
        "base_price": 4.75,
        "description": "Fresh passion fruit with green tea, tangy and sweet",
        "is_available": True
    },
    {
        "name": "Mango Smoothie",
        "base_price": 5.50,
        "description": "Fresh mango blended with ice and milk, tropical delight",
        "is_available": True
    },
    {
        "name": "Wintermelon Tea",
        "base_price": 4.25,
        "description": "Traditional wintermelon tea, naturally sweet and cooling",
        "is_available": True
    },
    {
        "name": "Oolong Milk Tea",
        "base_price": 4.75,
        "description": "Premium oolong tea with fresh milk, smooth and aromatic",
        "is_available": True
    },
    {
        "name": "Hokkaido Milk Tea",
        "base_price": 5.50,
        "description": "Rich Hokkaido milk with black tea, extra creamy",
        "is_available": True
    },
    {
        "name": "Strawberry Milk Tea",
        "base_price": 5.25,
        "description": "Fresh strawberry flavor with milk tea base, fruity and sweet",
        "is_available": True
    },
]

for drink_data in drinks_data:
    drink = Drink.objects.create(**drink_data)
    print(f"  ✓ Created drink: {drink.name} (${drink.base_price})")

print("\n" + "="*60)
print("✨ Database populated successfully!")
print("="*60)
print(f"\nSummary:")
print(f"  • {Size.objects.count()} sizes")
print(f"  • {Flavor.objects.count()} flavors")
print(f"  • {Topping.objects.count()} toppings")
print(f"  • {Drink.objects.count()} drinks")
print("\nYou can now start the server and browse the menu!")
