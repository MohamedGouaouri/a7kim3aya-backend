from django.shortcuts import render
from django.http import JsonResponse
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


def getAllProducts(request):
    # QuerySet object is not serializable
    products_query_set = Product.objects.all()
    products = [
        {'id': p.id, 'title': p.title, 'description': p.description, 'price': p.price}
        for p in products_query_set
    ]
    return JsonResponse(products, safe=False)


def getProductById(request, pid):
    try:
        db_product = Product.objects.get(id=pid)

        product = {
            'id': pid,
            'title': db_product.title,
            'description': db_product.description,
            'price': db_product.price
        }
        return JsonResponse(product)
    except Product.DoesNotExist:
        return JsonResponse({'result': 'product not found'})


def deleteById(request, pid):
    try:
        db_product = Product.objects.get(id=pid)
        db_product.delete()
        return JsonResponse({'status': 'ok'})
    except Product.DoesNotExist:
        return JsonResponse({'result': 'product not found'})
    except Exception:
        return JsonResponse({'result': 'Internal exception'})
