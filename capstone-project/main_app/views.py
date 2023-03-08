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
        name = Product.objects.filter(category=val).values('name').annotate(total=Count('name'))
        return render(request, 'main_app/category.html',locals())