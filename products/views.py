from django.shortcuts import render

from .models import Product

from .forms import ProdutForm


def home(request):
    data = {
        'name': "mohamed",
        'products': ['PC', 'Remote controller', 'Server'],
    }
    return render(request=request, template_name="home.html", context=data)


def about(request):

    # print(request.headers['Coockie'])
    return render(request=request, template_name="about.html", context={})


def product_details(request):
    p = Product.objects.get(id=1)
    return render(request, 'product/detail.html', {'p': p})


def create_product(request):
    form = ProdutForm(request.POST or None)
    if form.is_valid():
        form.save()
        print(request.POST['title'])

    return render(request, 'product/create_product.html', {'form': form})


def show(request, pid):
    # get the prduct id frm db

    p = Product.objects.get(id=pid)

    return render(request, 'product/detail.html', {'p': p})
