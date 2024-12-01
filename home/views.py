from django.shortcuts import render,redirect
from .models import *
from login.models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ItemForm


@login_required
def landing_view(request):
    user = request.user
    account_type = user.account.type
    cart = 0
    if account_type != 'business':
        product_objects = Items.objects.all()
        cart = Cart.objects.get(account = user.account).get_items()
        #search logic
        search_query = request.GET.get('search')
        if search_query != '' and search_query:
            searched_items = product_objects.filter(item_name__icontains = search_query)
            product_objects = searched_items

        paginator = Paginator(product_objects, per_page=3)
        page = request.GET.get('page')
        product_objects = paginator.get_page(page)
        
    else:
        product_objects = Items.objects.filter(seller = user.account)

        #search logic
        search_query = request.GET.get('search')
        if search_query != '' and search_query:
            searched_items = product_objects.filter(item_name__icontains = search_query)
            product_objects = searched_items

        paginator = Paginator(product_objects, per_page=3)
        page = request.GET.get('page')
        product_objects = paginator.get_page(page)
    return render(request, "home/landing.html", context={'product_objects':product_objects, 'cart':cart})

def detailsView(request, id):
    product = Items.objects.get(pk = id)
    if request.method == 'POST':
        cart = Cart.objects.get(account = request.user.account)
        data = request.POST
        quantity = int(data['quantity'][0])
        cart.add_item(str(id), quantity)
        print('Item Added')
    return render(request, 'home/details.html', context={'product': product})

@csrf_exempt
def update_model(request):
    if request.method == "POST":
        cart = Cart.objects.get(account = request.user.account)
        data = request.POST
        some_field = data.get('some_field')
        cart.add_item(str(some_field))
        return redirect('landing:index')
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def checkout(request):
    cart = Cart.objects.filter(account = request.user.account).first()
    item_list = []
    total = 0
    for key in cart.items:
        item = Items.objects.get(pk = int(key))
        item_list += [{
            'name':item.item_name,
            'price':item.item_price,
            'quantity':cart.items[key]
        },]
        total += item.item_price * cart.items[key]

    if request.method=='POST':
        cart.clear_cart()
        return JsonResponse({'status': 'ok', 'redirect_url': '/home/'})

    return render(request, 'home/checkout.html', context={'item_list':item_list, 'total':total})

def add_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        img = request.FILES.get('item_image')
        if img:
            new_item = Items.objects.create(
                seller = request.user.account,
                item_name = data['item_name'],
                item_desc = data['item_desc'],
                item_rating = data['item_rating'],
                item_price = data['item_price'],
                item_img = img
            )
        else:
            new_item = Items.objects.create(
                seller = request.user.account,
                item_name = data['item_name'],
                item_desc = data['item_desc'],
                item_rating = data['item_rating'],
                item_price = data['item_price']
            )
        new_item.save()
        return redirect('landing:index')
    return render(request, 'home/add_item.html', context={'form':form})