from django.db.models import Count
from django.shortcuts import render
from django.views import View
from . models import Product

# Create your views here.
def home(request):
    return render(request, 'main_app/home.html')

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        name = Product.objects.filter(category=val).values('name')
        return render(request, 'main_app/category.html',locals())
    
class CategoryName(View):
    def get(self, request, val):
        product = Product.objects.filter(name=val)
        name = Product.objects.filter(category=product[0].category).values('name')
        return render(request, 'main_app/category.html',locals())
    
class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'main_app/productdetail.html',locals())