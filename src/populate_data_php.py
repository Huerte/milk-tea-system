"""
Populate database with realistic milk tea products and options (Philippine Peso pricing)
Run this script with: Get-Content populate_data_php.py | py manage.py shell
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
    {"name": "Taro", "additional_price": 15.00},
    {"name": "Matcha", "additional_price": 20.00},
    {"name": "Chocolate", "additional_price": 15.00},
    {"name": "Strawberry", "additional_price": 15.00},
    {"name": "Mango", "additional_price": 20.00},
    {"name": "Honeydew", "additional_price": 15.00},
    {"name": "Lavender", "additional_price": 25.00},
    {"name": "Ube (Purple Yam)", "additional_price": 20.00},
    {"name": "Wintermelon", "additional_price": 15.00},
]

for flavor_data in flavors_data:
    flavor = Flavor.objects.create(**flavor_data)
    print(f"  ✓ Created flavor: {flavor.name} (+₱{flavor.additional_price})")


print("\nCreating toppings...")
toppings_data = [
    {"name": "Tapioca Pearls (Black)", "price": 20.00},
    {"name": "Crystal Boba", "price": 25.00},
    {"name": "Grass Jelly", "price": 20.00},
    {"name": "Aloe Vera", "price": 20.00},
    {"name": "Egg Pudding", "price": 25.00},
    {"name": "Red Bean", "price": 25.00},
    {"name": "Coconut Jelly", "price": 20.00},
    {"name": "Popping Boba (Assorted)", "price": 30.00},
    {"name": "Cheese Foam", "price": 35.00},
    {"name": "Nata de Coco", "price": 20.00},
    {"name": "Sago Pearls", "price": 20.00},
]

for topping_data in toppings_data:
    topping = Topping.objects.create(**topping_data)
    print(f"  ✓ Created topping: {topping.name} (+₱{topping.price})")


print("\nCreating drinks...")
drinks_data = [
    {
        "name": "Classic Milk Tea",
        "base_price": 85.00,
        "description": "Traditional black tea with creamy milk, a timeless Filipino favorite",
        "is_available": True
    },
    {
        "name": "Brown Sugar Boba Milk",
        "base_price": 120.00,
        "description": "Fresh milk with rich brown sugar syrup and chewy tapioca pearls",
        "is_available": True
    },
    {
        "name": "Thai Milk Tea",
        "base_price": 95.00,
        "description": "Authentic Thai tea with condensed milk, sweet and aromatic",
        "is_available": True
    },
    {
        "name": "Taro Milk Tea",
        "base_price": 110.00,
        "description": "Creamy taro blended with milk, naturally sweet and purple",
        "is_available": True
    },
    {
        "name": "Matcha Latte",
        "base_price": 125.00,
        "description": "Premium Japanese matcha powder with steamed milk",
        "is_available": True
    },
    {
        "name": "Jasmine Green Tea",
        "base_price": 75.00,
        "description": "Fragrant jasmine green tea, light and refreshing",
        "is_available": True
    },
    {
        "name": "Passion Fruit Tea",
        "base_price": 95.00,
        "description": "Fresh passion fruit with green tea, tangy and sweet",
        "is_available": True
    },
    {
        "name": "Mango Smoothie",
        "base_price": 115.00,
        "description": "Fresh Philippine mango blended with ice and milk, tropical delight",
        "is_available": True
    },
    {
        "name": "Wintermelon Tea",
        "base_price": 80.00,
        "description": "Traditional wintermelon tea, naturally sweet and cooling",
        "is_available": True
    },
    {
        "name": "Oolong Milk Tea",
        "base_price": 90.00,
        "description": "Premium oolong tea with fresh milk, smooth and aromatic",
        "is_available": True
    },
    {
        "name": "Hokkaido Milk Tea",
        "base_price": 120.00,
        "description": "Rich Hokkaido milk with black tea, extra creamy",
        "is_available": True
    },
    {
        "name": "Strawberry Milk Tea",
        "base_price": 105.00,
        "description": "Fresh strawberry flavor with milk tea base, fruity and sweet",
        "is_available": True
    },
    {
        "name": "Ube Milk Tea",
        "base_price": 115.00,
        "description": "Filipino purple yam (ube) blended with milk tea, uniquely Filipino",
        "is_available": True
    },
    {
        "name": "Salted Caramel Milk Tea",
        "base_price": 110.00,
        "description": "Sweet and salty caramel with creamy milk tea",
        "is_available": True
    },
    {
        "name": "Lychee Fruit Tea",
        "base_price": 95.00,
        "description": "Sweet lychee fruit with refreshing green tea",
        "is_available": True
    },
]

for drink_data in drinks_data:
    drink = Drink.objects.create(**drink_data)
    print(f"  ✓ Created drink: {drink.name} (₱{drink.base_price})")

print("\n" + "="*60)
print("✨ Database populated successfully with Philippine Peso pricing!")
print("="*60)
print(f"\nSummary:")
print(f"  • {Size.objects.count()} sizes")
print(f"  • {Flavor.objects.count()} flavors")
print(f"  • {Topping.objects.count()} toppings")
print(f"  • {Drink.objects.count()} drinks")
print("\n💡 Price Range: ₱75 - ₱125 (base price)")
print("   Add-ons: ₱15 - ₱35 each")
print("\nYou can now start the server and browse the menu!")
