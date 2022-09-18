from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from cart.models import CartItem
from cart.views import _cart_id
from category.models import Category
from store.models import Product
# Create your views here.

def store(request,category_slug=None):
    categories=None
    Products=None

    if category_slug != None:
        categories=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.filter(category=categories,is_available=True)
        paginator=Paginator(products,6 )
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)
        product_count=products.count()
    else:
        products=Product.objects.all().filter(is_available=True)
        paginator=Paginator(products,2)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)
        product_count=products.count()
        print(paged_products)
        print(paged_products.object_list)
        # print(paged_products.next_page_number())
    #     url:http://localhost:7001/store/
    #  -->view store()function
    #  -->database get products
    #  -->products inject into paginator and group
    #     eg: <QuerySet [<Product: atx-jeans>, <Product: blue-shirt>]>
    #  get_page()->get a group of paginator
    # then return to front_end



    context={
        'products':paged_products,
        'product_count':product_count,
        'paginator_num_pages':paginator.num_pages,

    }
    return render(request,'store/store.html',context)

def product_detail(request,category_slug=None,product_slug=None):
    try:
        single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
        in_cart=CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()
    except Exception as e:
        raise e
    context={
        'single_product':single_product,
        'in_cart':in_cart,
    }
    return render(request,'store/product_detail.html',context)