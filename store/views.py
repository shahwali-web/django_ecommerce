from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


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
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, 'You have Register Successfully!!! Welcome')
            return redirect('login')
        else:
            messages.success(request, 'WOOPS You have Problem Try Again to Register!!!')

            return redirect('register')

    return render(request, 'register.html', {'form': form})











