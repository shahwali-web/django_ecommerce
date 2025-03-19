from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from .forms import SignUpForm, UserFormUpdate, ChangePasswordForm, UserInfoForm
from decimal import Decimal, InvalidOperation





def search(request):
    if request.method == 'POST':
        searched = request.POST.get('searched').strip()
        try:
            searched = int(searched)
            searched = Product.objects.filter(
                Q(price__exact=searched) |
                Q(sale_price__exact=searched)
            )

        except ValueError:

            if searched:
                searched = Product.objects.filter(
                    Q(name__icontains=searched) |
                    Q(description__icontains=searched)
                )

        # if search product does not exist then print this message
        if not searched:
            messages.error(request, "No matching products found.")

        context = {"searched": searched}
        return render(request, 'search.html', context=context)
    else:
        return render(request, 'search.html')



























def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Info is Updated')
            return redirect('home')
        return render(request, 'update_info.html', {'form': form})
    else:
        messages.success(request, "You Must be logged in To update info!")
        return redirect('login')


def update_password(request):
    if not request.user.is_authenticated:
        messages.success(request, "Sorry You must Login to Update password")

    current_user = request.user
    if request.method == "POST":
        form = ChangePasswordForm(current_user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password is Successfully Changed")
            login(request, current_user)
            return redirect('home')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
                return redirect('update_password')
    else:
        form = ChangePasswordForm(current_user)
        return render(request, 'update_password.html', {"form": form})


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UserFormUpdate(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, "User has been Updated!!!")
            return redirect('update_user')
        return render(request, 'update_user.html', {"user_form": user_form})
    else:
        messages.success(request, "You must be login to access that page! ")
        return redirect('home')

def category_summary(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request,'category_summary.html', context=context)

def category(request, foo):
    foo = foo.replace('-',' ')

    try:
        category = Category.objects.get(name=foo)
        prodcuts = Product.objects.filter(category=category)

        return render(request, 'category.html', {'products': prodcuts, 'category': category})
    except:
        messages.success(request, "Sorry this Category does not exits")
        return redirect('home')

def categories(request):
    return {'categories': Category.objects.all()}


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {"product": product})
def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You have been login! ")
            return redirect('home')
        else:
            messages.success(request,"Please enter correct detail to  login Error! ")
            return redirect('login')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "Logout we will see you soon! ")

    return redirect('login')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have Register Successfully!!! Welcome')
            return redirect('update_info')
        else:
            messages.success(request, 'WOOPS You have Problem Try Again to Register!!!')

            return redirect('register')

    return render(request, 'register.html', {'form': form})











