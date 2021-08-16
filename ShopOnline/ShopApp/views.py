from django.shortcuts import render, redirect
from .models import Category, Item, Order
from .forms import OrderForm, UserRegistrationForm


def home(request):

    items = Item.objects.all().order_by('-added')[:3]

    return render(request, 'home.html', {'items':items})

def item(request, item_id):

    item = Item.objects.get(id = item_id)

    return render(request, 'item.html', {'item':item})

def categories(request):

    return {'categories': Category.objects.all()}

def category(request, category_id):
    
    category = Category.objects.get(id = category_id)
    items = Item.objects.filter(category=category)

    return render(request, "category.html", {'category':category, 'items':items})

def all_items(request):

    categories = Category.objects.all()

    return render(request, 'all.html', {'categories':categories})

def cart(request):

    if request.method == "POST":

        form = OrderForm(request.POST, request.FILES)

        if form.is_valid():

            order = Order()

            order.items = request.POST.get('items', '')            
            order.name = form.cleaned_data['name']
            order.surname = form.cleaned_data['surname']
            order.email = form.cleaned_data['email']
            order.address = form.cleaned_data['address']
            order.city = form.cleaned_data['city']

            order.save()

            return redirect('order_done')
    else:
        form = OrderForm()

    return render(request, 'cart.html', {'form':form})

def order_done(request):
    return render(request, 'order_done.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            
            new_user = user_form.save(commit=False)
            
            new_user.set_password(user_form.cleaned_data['password'])
            
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})