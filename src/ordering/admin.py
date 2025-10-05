from django.contrib import admin
from .models import Drink, Flavor, Topping, Size, Order, OrderItem, Payment


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'base_price', 'is_available']
    list_filter = ['is_available']


@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    list_display = ['name', 'additional_price']


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_multiplier']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'status', 'total_amount', 'created_at']
    list_filter = ['status', 'created_at']
    inlines = [OrderItemInline]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['order', 'payment_method', 'amount', 'status', 'created_at']
    list_filter = ['payment_method', 'status', 'created_at']
