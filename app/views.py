from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(req):
    form = CreateUserForm()

    if req.method == "POST":
        form = CreateUserForm(req.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(req, 'app/register.html', context)
def Login(req):
    context = {}
    return render(req, 'app/Login.html', context)
def home(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer =customer, complete= False)
        items = order.orderitem_set.all();
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items'] 
    products = Product.objects.all()
    context={'products':products, 'cartItems':cartItems}
    return render(req,'app/home.html',context)

def cart(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer =customer, complete= False)
        items = order.orderitem_set.all();
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    context={'items':items, 'order':order, 'cartItems':cartItems }
    return render(req,'app/cart.html',context)

def checkout(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer =customer, complete= False)
        items = order.orderitem_set.all();
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    context={'items':items, 'order':order, 'cartItems':cartItems }
    return render(req,'app/checkout.html',context)

def updateItem(req):
    data = json.loads(req.body)
    productId = data['productId']
    action = data['action']
    customer = req.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer =customer, complete= False)
    orderItem, created = OrderItem.objects.get_or_create(order =order, product= product)
    if action=='add':
        orderItem.quantity +=1
    elif action == 'remove':
        orderItem.quantity -=1
    orderItem.save()
    if orderItem.quantity<=0:
        orderItem.delete()
    return JsonResponse('added',safe=False)