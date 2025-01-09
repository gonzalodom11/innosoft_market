from cart.cart import Cart
from django.shortcuts import render

from orders.tasks import order_created
from .forms import OrderCreateForm
from .models import OrderItem

def order_create(request):
    cart = Cart(request)
    
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            
            # clear the cart
            cart.clear()
            # launch asynchronous task, delay method is a mechanism of Celery tasks
            order_created.delay(order.id)
            
            return render(
                request, 'orders/order/created.html', {'order': order}
            )
    else:
        form = OrderCreateForm()
        
    return render(
        request,
        'orders/order/create.html',
        {'cart': cart, 'form': form}
    )