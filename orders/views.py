from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem

@login_required 
def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
                product = item['product']
                product.stock -= item['quantity']
                product.save()
            cart.clear()
            return render(request, 'orders/order_created.html', {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order_create.html', {
        'cart': cart,
        'form': form
    })
def order_history(request):
    orders = request.user.orders.all()
    return render(request, 'orders/order_history.html', {'orders': orders})
# Create your views here.
