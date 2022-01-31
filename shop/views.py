from django.shortcuts import render, get_object_or_404

from cart.forms import Add2CartForm
from shop.models import Product, Category
from shop.forms import ProductNameForm


def home(request, slug=None):
    products = Product.objects.filter(status=True)
    categories = Category.objects.filter(is_sub=False)
    search = ProductNameForm()
    if slug:
        category = get_object_or_404(Category, slug=slug)
        sub_categories = list(category.sub_categories.all())
        products = products.filter(category__in=[category] + sub_categories)

    if request.POST:
        form = ProductNameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['product_name']
            products = products.filter(name__contains=name)
    return render(request, 'shop/home.html', {'products': products, 'categories': categories, "search": search})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    form = Add2CartForm()
    return render(request, 'shop/product_detail.html', {'product': product, 'form': form})
