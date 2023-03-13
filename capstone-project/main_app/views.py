from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View
from . models import Product, Customer
from . forms import CustomerProfileForm, CustomerRegistrationForm
from django.contrib import messages

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
    

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'main_app/signup.html', locals())
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! Sign-Up Successful")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'main_app/signup.html', locals())
    
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'main_app/profile.html', locals())
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            reg = Customer(user=user,name=name)
            reg.save()
            messages.success(request, "Success!")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'main_app/profile.html', locals())

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'main_app/address.html', locals())

class updateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'main_app/updateAddress.html', locals())
    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.save()
            messages.success(request, "Profile Updated Successfully!")
        else:
            messages.warning(request, "Something went wrong please try again")
        return redirect("address")