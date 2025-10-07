from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Drink, Flavor, Topping, Size, Order, OrderItem, Payment
import json


def enter_system(request):
    
    return render(request, 'ordering/enter_system.html')


def browse_menu(request):
    
    drinks = Drink.objects.filter(is_available=True)
    flavors = Flavor.objects.all()
    toppings = Topping.objects.all()
    sizes = Size.objects.all()
    
    context = {
        'drinks': drinks,
        'flavors': flavors,
        'toppings': toppings,
        'sizes': sizes,
    }
    return render(request, 'ordering/browse_menu.html', context)


def decide_order(request):
    


    return redirect('choose_specifics')


def choose_specifics(request):
    
    if request.method == 'POST':

        drink_id = request.POST.get('drink_id')
        size_id = request.POST.get('size_id')
        flavor_id = request.POST.get('flavor_id')
        topping_ids = request.POST.getlist('toppings')
        quantity = int(request.POST.get('quantity', 1))
        
        drink = get_object_or_404(Drink, id=drink_id)
        size = get_object_or_404(Size, id=size_id)
        flavor = get_object_or_404(Flavor, id=flavor_id) if flavor_id else None
        toppings = Topping.objects.filter(id__in=topping_ids)
        

        item_price = drink.base_price * size.price_multiplier
        if flavor:
            item_price += flavor.additional_price
        item_price += sum(topping.price for topping in toppings)
        item_price *= quantity
        

        current_item = {
            'drink_name': drink.name,
            'drink_id': drink_id,
            'size_name': size.name,
            'size_id': size_id,
            'flavor_name': flavor.name if flavor else None,
            'flavor_id': flavor_id,
            'toppings': [{'name': t.name, 'id': t.id} for t in toppings],
            'quantity': quantity,
            'item_price': float(item_price)
        }
        
        request.session['current_item'] = current_item
        

        return redirect('choose_payment_method')
    

    drinks = Drink.objects.filter(is_available=True)
    flavors = Flavor.objects.all()
    toppings = Topping.objects.all()
    sizes = Size.objects.all()
    
    context = {
        'drinks': drinks,
        'flavors': flavors,
        'toppings': toppings,
        'sizes': sizes,
    }
    return render(request, 'ordering/choose_specifics.html', context)


def choose_payment_method(request):
    
    current_item = request.session.get('current_item')
    
    if not current_item:
        messages.error(request, 'No item selected. Please choose your drink first.')
        return redirect('choose_specifics')
    
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        

        current_item['payment_method'] = payment_method
        request.session['current_item'] = current_item
        

        return redirect('proceed_to_counter')
    
    return render(request, 'ordering/choose_payment_method.html', {'current_item': current_item})


def proceed_to_counter(request):
    
    current_item = request.session.get('current_item')
    
    if not current_item:
        messages.error(request, 'No item selected. Please start your order.')
        return redirect('browse_menu')
    
    if not current_item.get('payment_method'):
        messages.error(request, 'Please select a payment method first.')
        return redirect('choose_payment_method')
    
    return render(request, 'ordering/proceed_to_counter.html', {'current_item': current_item})


def place_order(request):
    
    if request.method == 'POST':
        current_item = request.session.get('current_item')
        
        if not current_item:
            messages.error(request, 'No item found. Please start over.')
            return redirect('browse_menu')
        

        order = Order.objects.create(
            order_number=Order().generate_order_number(),
            total_amount=current_item['item_price']
        )
        

        drink = Drink.objects.get(id=current_item['drink_id'])
        size = Size.objects.get(id=current_item['size_id'])
        flavor = Flavor.objects.get(id=current_item['flavor_id']) if current_item['flavor_id'] else None
        
        order_item = OrderItem.objects.create(
            order=order,
            drink=drink,
            size=size,
            flavor=flavor,
            quantity=current_item['quantity'],
            item_price=current_item['item_price']
        )
        

        if current_item.get('toppings'):
            for topping_data in current_item['toppings']:
                topping = Topping.objects.get(id=topping_data['id'])
                order_item.toppings.add(topping)
        

        payment = Payment.objects.create(
            order=order,
            payment_method=current_item['payment_method'],
            amount=order.total_amount,
            status='completed',
            transaction_id=f'TXN_{order.order_number}'
        )
        

        order.status = 'placed'
        order.save()
        

        request.session['current_item'] = None
        
        return redirect('wait_for_drink', order_number=order.order_number)
    
    return redirect('proceed_to_counter')




def process_payment(request):
    
    messages.info(request, 'Payment method is now selected earlier in the process.')
    return redirect('browse_menu')


def wait_for_drink(request, order_number):
    
    order = get_object_or_404(Order, order_number=order_number)
    return render(request, 'ordering/wait_for_drink.html', {'order': order})


def receive_drink(request, order_number):
    
    order = get_object_or_404(Order, order_number=order_number)
    
    if request.method == 'POST':

        order.status = 'completed'
        order.save()
        return redirect('enjoy_drink', order_number=order_number)
    

    if order.status == 'placed':
        order.status = 'ready'
        order.save()
    
    return render(request, 'ordering/receive_drink.html', {'order': order})


def enjoy_drink(request, order_number):
    
    order = get_object_or_404(Order, order_number=order_number)
    return render(request, 'ordering/enjoy_drink.html', {'order': order})


def exit_website(request):
    

    request.session.flush()
    return render(request, 'ordering/exit_website.html')



@csrf_exempt
def update_order_status(request, order_number):
    
    if request.method == 'POST':
        order = get_object_or_404(Order, order_number=order_number)
        data = json.loads(request.body)
        new_status = data.get('status')
        
        if new_status in ['placed', 'preparing', 'ready', 'completed']:
            order.status = new_status
            order.save()
            return JsonResponse({'success': True, 'status': order.status})
    
    return JsonResponse({'success': False})


def get_order_status(request, order_number):
    
    order = get_object_or_404(Order, order_number=order_number)
    return JsonResponse({
        'status': order.status,
        'order_number': order.order_number,
        'total_amount': str(order.total_amount)
    })
