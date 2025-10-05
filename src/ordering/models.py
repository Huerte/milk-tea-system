from django.db import models
from django.utils import timezone


class Drink(models.Model):
    """Model for milk tea drinks"""
    name = models.CharField(max_length=100)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Flavor(models.Model):
    """Model for drink flavors"""
    name = models.CharField(max_length=50)
    additional_price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.name


class Topping(models.Model):
    """Model for drink toppings"""
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} (+${self.price})"


class Size(models.Model):
    """Model for drink sizes"""
    name = models.CharField(max_length=20)  # Small, Medium, Large
    price_multiplier = models.DecimalField(max_digits=3, decimal_places=2, default=1.00)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    """Model for customer orders"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('placed', 'Placed'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
        ('completed', 'Completed'),
    ]
    
    order_number = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order #{self.order_number}"
    
    def generate_order_number(self):
        """Generate unique order number"""
        import random
        import string
        while True:
            number = ''.join(random.choices(string.digits, k=6))
            if not Order.objects.filter(order_number=number).exists():
                return number


class OrderItem(models.Model):
    """Model for individual items in an order"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE, null=True, blank=True)
    toppings = models.ManyToManyField(Topping, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def calculate_price(self):
        """Calculate total price for this item"""
        base_price = self.drink.base_price * self.size.price_multiplier
        if self.flavor:
            base_price += self.flavor.additional_price
        
        toppings_price = sum(topping.price for topping in self.toppings.all())
        return (base_price + toppings_price) * self.quantity
    
    def save(self, *args, **kwargs):
        self.item_price = self.calculate_price()
        super().save(*args, **kwargs)


class Payment(models.Model):
    """Model for order payments"""
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Payment for Order #{self.order.order_number}"
