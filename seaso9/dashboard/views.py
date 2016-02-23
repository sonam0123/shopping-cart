from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm, LoginForm, ProductForm, OrderForm
from inventory.models import Product
from shop.models import Order


def registration_form(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                password=form.cleaned_data['password']
            )
            user.save()
            messages.success(request, 'You have successfully registered.')
            return redirect(reverse('dashboard:login'))
        else:
            return render(request, "registration_form.html", {"form": form})
    else:
        form = RegisterForm()
        return render(request, "registration_form.html", {"form": form})


@login_required
def userList(request):
    if request.method == 'GET':
        users = User.objects.all()
        return render(request, "users.html", {"users": users})


@login_required
def updateuser(request, pk):
    instance = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = RegisterForm(request.POST or None, instance=instance)
        if form.is_valid():
            instance.save()
            return render(request ,"success.html")
        else:
            return render(request,"update.html",{"form":form})
    else:
        form = RegisterForm(request.POST or None, instance=instance)
        return render(request,"update.html",{"form":form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Welcome!')
                    next_url = request.GET.get('next', None)
                    if next_url:
                        return redirect(next_url)
                    return redirect(reverse('dashboard:home'))
            else:
                messages.error(request, 'Invalid username or password')
                return render(request, "dashboard/login.html", {'form': form})
        else:
            return render(request, 'dashboard/login.html', {'form': form})
    else:
        form = LoginForm()
        next = request.GET.get('next', None)
        return render(request, "dashboard/login.html", {'form': form, 'next': next})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('dashboard:login'))


@login_required
def deleteuser(request, pk):
    if request.method == 'POST':
        user=get_object_or_404(User, pk=pk)
        user.delete()
        return redirect('dashboard:user_list')
    else:
        return HttpResponse(staus=405)


@login_required
def home(request):
    return render(request, 'dashboard/home.html')


@login_required
def products_list(request):
    products = Product.objects.all()
    return render(request, 'dashboard/products_list.html', {'products': products})


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:products_list')
        else:
            return render(request, 'dashboard/product_form.html', {'form': form})
    else:
        form = ProductForm()
        return render(request, 'dashboard/product_form.html', {'form': form})


@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.delete()
        return redirect(reverse('dashboard:products_list'))
    else:
        return render(request, 'dashboard/product_confirm_delete.html', {'product': product})



@login_required
def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard:products_list'))
        else:
            return render(request, 'dashbard/product_form.html', {'form': form})
    else:
        form = ProductForm(request.POST or None, instance=product)
        return render(request, 'dashboard/product_form.html', {'form': form})

# ------- Orders-

@login_required
def orders_list(request):
    orders = Order.objects.all()
    return render(request, 'dashboard/orders_list.html', {'orders': orders})

@login_required
def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return render(request, 'dashboard/order_detail.html', {'order': order})


@login_required
def delete_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == "POST":
        order.delete()
        return redirect(reverse('dashboard:orders_list'))
    else:
        return render(request, 'dashboard/order_confirm_delete.html', {'order': order})


@login_required
def update_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order updated.')
            return redirect(reverse('dashboard:orders_list'))
        else:
            return render(request, 'dashbard/order_form.html', {'form': form})
    else:
        form = OrderForm(instance=order)
        return render(request, 'dashboard/order_form.html', {'form': form})
