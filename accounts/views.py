from django.shortcuts import render, redirect
from .forms import *
from django.forms import inlineformset_factory
from .filters import OrderFilter
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only
from .models import *


def is_valid_queryparam(param):
    return param != '' and param is not None


# LOGIN AND USER REGISTRATION VIEWS
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + username)
            return redirect('login')

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username OR Password is incorrect!")

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


# DASHBOARD VIEW
@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all().order_by('-date_created')
    customers = Customer.objects.all().order_by('-date_created')
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    out_for_delivery = orders.filter(status='Out for delivery').count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
        'out_for_delivery': out_for_delivery,
        'total_customers':  total_customers,
        'myFilter': myFilter,
    }
    return render(request, 'accounts/dashboard.html', context)


# USER PAGE
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    out_for_delivery = orders.filter(status='Out for delivery').count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'orders': orders,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
        'out_for_delivery': out_for_delivery,
        'myFilter': myFilter,
    }
    return render(request, 'accounts/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST or None, request.FILES or None, instance=customer)
        if form.is_valid():
            form.save()
    else:
        form=CustomerForm()

    context = {'form': form, }
    return render(request, 'accounts/account_settings.html', context)


# CUSTOMER VIEWS that the Admin only can access
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all().order_by('-date_created')
    total_orders = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'customer': customer,
        'orders': orders,
        'total_orders': total_orders,
        'myFilter': myFilter,
    }
    return render(request, 'accounts/customers.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def CreateCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'accounts/create_customer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def UpdateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'accounts/create_customer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def DeleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('/')
    context = {
        'customer': customer,
    }
    return render(request, 'accounts/delete_customer.html', context)


# PRODUCT VIEW
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all().order_by('-date_created')
    total_products = products.count()
    context = {
        'products': products,
        'total_products': total_products,
    }
    return render(request, 'accounts/products.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def CreateProduct(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('products')
    context = {
        'form': form,
    }
    return render(request, 'accounts/create_product.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def UpdateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {
        'form': form,
    }
    return render(request, 'accounts/update_product.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def DeleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    context = {
        'product': product,
    }
    return render(request, 'accounts/delete_product.html', context)


# ORDER VIEWS
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def CreateOrder(request, pk):
    OrderFormSet = inlineformset_factory(
        Customer, Order, fields=('product', 'category', 'status'), extra=5)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {
        'formset': formset,
    }
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def UpdateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'accounts/update_order.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def DeleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {
        'order': order,
    }
    return render(request, 'accounts/delete_order.html', context)
