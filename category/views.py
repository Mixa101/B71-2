# Create your views here.


from django.http.request import HttpRequest
from django.shortcuts import render

from category.models import Product


def product_list(request: HttpRequest):
    products = Product.objects.filter()

    price_order = request.GET.get("price_order")

    if price_order:
        if price_order == "gte":
            products = products.order_by("price")
        else:
            products = products.order_by("-price")
    price_min = request.GET.get("price_min")
    price_max = request.GET.get("price_max")
    if price_min:
        products = products.filter(price__gte=price_min)

    if price_max:
        products = products.filter(price__lte=price_max)

    search = request.GET.get("search")

    if search:
        products = products.filter(name__icontains=search)

    return render(request, "list.html", {"products": products})


def product_detail(request: HttpRequest, id):
    product = Product.objects.get(id=id)

    return render(request, "detail.html", {"product": product})
