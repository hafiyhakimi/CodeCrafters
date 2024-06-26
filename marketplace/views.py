from django.shortcuts import render
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
# from LOGIN.models import Person as FarmingPerson
# from LOGIN.models import Feed, Booking, Workshop, Group, Member 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
# from .forms import CreateInDiscussion, PersonForm, UserUpdateForm
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.db.models.signals import post_save
from django.dispatch import receiver
from cryptography.fernet import Fernet
from member.models import Person
# from sharing.models import Feed
from .models import prodProduct, prodStock
from basket.models import Basket, prodReview
import re
from .forms import ProductForm, ProductStockForm
# from .models import Person

# Create your views here.


#marketplace
# def mainMarketplace(request):
#     try:
#         marketplace=MarketplaceFeed.objects.all()
#         return render(request,'MainMarketplace.html',{'marketplace':marketplace})
#     except MarketplaceFeed.DoesNotExist:
#         raise Http404('Data does not exist')
    
def mainMarketplace(request):
    try:
        marketplace=prodProduct.objects.all()
        
        # Create a dictionary to store product and stock pairs
        product_stock_pairs = []

        for product in marketplace:
            stock = prodStock.objects.filter(product=product).first()
            product_stock_pairs.append({
                'product': product,
                'stock': stock
            })
        
        person = Person.objects.get(Email=request.session['Email'])
        
        allBasket = Basket.objects.filter(Person_fk_id=person.id,is_checkout=0)
        user=Person.objects.all()
        return render(request,'MainMarketplace.html',{'product_stock_pairs': product_stock_pairs, 'allBasket':allBasket, 'person':person, 'user':user})
    except prodProduct.DoesNotExist:
        raise Http404('Data does not exist')
    
def myMarketplace(request):
    try:
        person = Person.objects.get(Email=request.session['Email'])
        marketplace=prodProduct.objects.filter(Person_fk=person)
        allBasket = Basket.objects.filter(Person_fk_id=person.id,is_checkout=0)
        user=Person.objects.all()
        return render(request,'MyMarketplace.html',{'marketplace':marketplace, 'allBasket':allBasket, 'person':person, 'user':user})
    except prodProduct.DoesNotExist:
        raise Http404('Data does not exist')
    
def viewProduct(request,pk):
    try:
        person=Person.objects.get(Email=request.session['Email'])
        product = prodProduct.objects.get(productid=pk)
        reviews = prodReview.objects.filter(productid=product)
        allBasket = Basket.objects.filter(Person_fk_id=person.id,is_checkout=0)
        stock = prodStock.objects.get(product_id=pk)
            
        return render(request,'ViewProduct.html',{'product':product, 'stock': stock, 'person':person, 'allBasket':allBasket, 'reviews':reviews})
    except prodProduct.DoesNotExist:
        raise Http404('Data does not exist')
    
def viewSeller(request,pk):
    try:
        person=Person.objects.get(Email=request.session['Email'])
        seller = Person.objects.get(id=pk)
        products = prodProduct.objects.filter(Person_fk=seller)
        allBasket = Basket.objects.filter(Person_fk_id=person.id,is_checkout=0)
        
        # Create a dictionary to store product and stock pairs
        product_stock_pairs = []

        for product in products:
            stock = prodStock.objects.filter(product=product).first()
            product_stock_pairs.append({
                'product': product,
                'stock': stock
        })
            
        return render(request,'ViewSeller.html',{'product_stock_pairs': product_stock_pairs, 'person':person, 'seller':seller, 'allBasket':allBasket})
    except Person.DoesNotExist:
        raise Http404('Seller does not exist')
    except prodProduct.DoesNotExist:
        raise Http404('Product does not exist')
    
# def sellProduct(request, fk1):
#     person = Person.objects.get(pk=fk1)
#     if request.method == 'POST':
#         product = prodProduct()
#         # Product Name Validation
#         product.productName = request.POST.get('productName')
#         if len(product.productName) > 30:
#             messages.error(request, 'Product name cannot be more than 30 characters.')
#             return redirect(request.META.get('HTTP_REFERER'))

#         # Product Description Validation
#         product.productDesc = request.POST.get('productDesc')
#         if len(product.productDesc) > 500:
#             messages.error(request, 'Product description cannot be more than 500 characters.')
#             return redirect(request.META.get('HTTP_REFERER'))
        
#         # Product Category Validation
#         product.productCategory = request.POST.get('productCategory')
#         customCategory = request.POST.get('customCategory')
#         if product.productCategory == "None Selected":
#             messages.error(request, 'Product category has to be selected')
#             return redirect(request.META.get('HTTP_REFERER'))
        
#         if product.productCategory == "Others" and customCategory:
#             # Use custom category if "Others" is selected and custom category is provided
#             product.productCategory = customCategory
#         else:
#             # Use the selected predefined category
#             product.productCategory = product.productCategory

#         # Product Price Validation
#         product.productPrice = request.POST.get('productPrice')
#         price_parts = product.productPrice.split('.')
#         # Regular expression to match digits and optional decimal point
#         price_pattern = r'^\d+(\.\d{1,2})?$'

#         # Check if the input matches the pattern
#         if not re.match(price_pattern, product.productPrice):
#             messages.error(request, 'Product price should only contain digits and allow up to two digits after the decimal point.')
#             return redirect(request.META.get('HTTP_REFERER'))
#         elif len(price_parts) == 1:
#             # No decimal point in the input, check if it consists of digits
#             if not product.productPrice.isdigit():
#                 messages.error(request, 'Product price should only contain digits.')
#                 return redirect(request.META.get('HTTP_REFERER'))
#         elif len(price_parts) == 2:
#             # Input contains a decimal point, check the digits before and after the decimal point
#             if not (price_parts[0].isdigit() and len(price_parts[1]) <= 2 and price_parts[1].isdigit()):
#                 messages.error(request, 'Product price should only contain digits and allow two digits after the decimal point.')
#                 return redirect(request.META.get('HTTP_REFERER'))
#         else:
#             # Input contains more than one decimal point, invalid format
#             messages.error(request, 'Invalid product price format.')
#             return redirect(request.META.get('HTTP_REFERER'))

#         # Product Stock Validation
#         product.productStock = request.POST.get('productStock')
#         if not product.productStock.isdigit():
#             messages.error(request, 'Product stock should only contain digits.')
#             return redirect(request.META.get('HTTP_REFERER'))
        
#         if len(request.FILES) != 0:
#             product.productPhoto = request.FILES['productPhoto']
        
#         fss = FileSystemStorage()
        
#         product.Person_fk=person
        
#         product.save()

#         messages.success(request,'Product Has Been Added Succesfully..!')

#         return redirect('marketplace:MainMarketplace')
#     else :
#         return render(request,'SellProduct.html')
    
def sellProduct(request, fk1):
    person = get_object_or_404(Person, pk=fk1)

    if request.method == 'POST':
        productform = ProductForm(request.POST, request.FILES)
        stockform = ProductStockForm(request.POST)
        
        if productform.is_valid() and stockform.is_valid():
            product = productform.save(commit=False)
            product.Person_fk = person
            
            # Custom validation for product name
            if len(product.productName) > 30:
                messages.error(request, 'Product name cannot be more than 30 characters.')
                return redirect(request.META.get('HTTP_REFERER'))

            # Custom validation for product description
            if len(product.productDesc) > 500:
                messages.error(request, 'Product description cannot be more than 500 characters.')
                return redirect(request.META.get('HTTP_REFERER'))

            # Custom validation for product category
            if product.productCategory == "None Selected":
                messages.error(request, 'Product category has to be selected')
                return redirect(request.META.get('HTTP_REFERER'))

            customCategory = request.POST.get('customCategory')
            if product.productCategory == "Others" and customCategory:
                product.productCategory = customCategory

            # Custom validation for product price
            price_pattern = r'^\d+(\.\d{1,2})?$'
            if not re.match(price_pattern, str(product.productPrice)):
                messages.error(request, 'Product price should only contain digits and allow up to two digits after the decimal point.')
                return redirect(request.META.get('HTTP_REFERER'))

            product.save()

            # Save stock form with the saved product instance
            stock = stockform.save(commit=False)
            stock.product = product

            # Custom validation for product stock
            if not str(stock.stock).isdigit():
                messages.error(request, 'Product stock should only contain digits.')
                product.delete()  # delete the saved product if stock validation fails
                return redirect(request.META.get('HTTP_REFERER'))

            stock.save()
            messages.success(request, 'Product Has Been Added Successfully..!')
            return redirect('marketplace:MainMarketplace')
        else:
            # Display form errors
            for field, errors in productform.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

            for field, errors in stockform.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        productform = ProductForm()
        stockform = ProductStockForm()

    return render(request, 'ProductForm.html', {'productform': productform, 'stockform': stockform, 'update': False, 'person': person})

def deleteProduct(request, fk1):
    try:
        product = prodProduct.objects.get(pk=fk1)
        product.delete()  # Call delete() on the product instance
        messages.success(request, 'The product has been deleted successfully.')
    except prodProduct.DoesNotExist:
        messages.error(request, 'The product does not exist.')
    return redirect('marketplace:MainMarketplace')

def restrictProduct(request, fk1):
    try:
        product = prodProduct.objects.get(pk=fk1)
        product.restricted = True
        product.save()
    except prodProduct.DoesNotExist:
        messages.error(request, 'The product does not exist.')
    return redirect('marketplace:MainMarketplace')

def unrestrictProduct(request, fk1):
    try:
        product = prodProduct.objects.get(pk=fk1)
        product.restricted = False
        product.save()
    except prodProduct.DoesNotExist:
        messages.error(request, 'The product does not exist.')
    return redirect('marketplace:MainMarketplace')

# def updateProduct(request, fk1):
#     product = prodProduct.objects.get(pk=fk1) 
#     if request.method == 'POST':
#         # Product Name Validation
#         product_name = request.POST.get('productName')
#         if len(product_name) > 20:
#             messages.error(request, 'Product name cannot be more than 20 characters.')
#             return redirect(request.META.get('HTTP_REFERER'))

#         # Product Description Validation
#         product_desc = request.POST.get('productDesc')
#         if len(product_desc) > 500:
#             messages.error(request, 'Product description cannot be more than 500 characters.')
#             return redirect(request.META.get('HTTP_REFERER'))
        
#         # Product Category Validation
#         product_category = request.POST.get('productCategory')
#         customCategory = request.POST.get('customCategory')
        
#         if product_category == "None Selected":
#             messages.error(request, 'Product category has to be selected')
#             return redirect(request.META.get('HTTP_REFERER'))
        
#         if product_category == "Others" and customCategory:
#             # Use custom category if "Others" is selected and custom category is provided
#             product_category = customCategory
#         else:
#             # Use the selected predefined category
#             product_category = product_category

#         # Product Price Validation
#         product_price = request.POST.get('productPrice')
#         price_parts = product_price.split('.')
#         # Regular expression to match digits and optional decimal point
#         price_pattern = r'^\d+(\.\d{1,2})?$'

#         # Check if the input matches the pattern
#         if not re.match(price_pattern, product_price):
#             messages.error(request, 'Product price should only contain digits and allow up to two digits after the decimal point.')
#             return redirect(request.META.get('HTTP_REFERER'))
#         elif len(price_parts) == 1:
#             # No decimal point in the input, check if it consists of digits
#             if not product_price.isdigit():
#                 messages.error(request, 'Product price should only contain digits.')
#                 return redirect(request.META.get('HTTP_REFERER'))
#         elif len(price_parts) == 2:
#             # Input contains a decimal point, check the digits before and after the decimal point
#             if not (price_parts[0].isdigit() and len(price_parts[1]) <= 2 and price_parts[1].isdigit()):
#                 messages.error(request, 'Product price should only contain digits and allow two digits after the decimal point.')
#                 return redirect(request.META.get('HTTP_REFERER'))
#         else:
#             # Input contains more than one decimal point, invalid format
#             messages.error(request, 'Invalid product price format.')
#             return redirect(request.META.get('HTTP_REFERER'))

#         # Product Stock Validation
#         product_stock = request.POST.get('productStock')
#         if not product_stock.isdigit():
#             messages.error(request, 'Product stock should only contain digits.')
#             return redirect(request.META.get('HTTP_REFERER'))
        
#         product.productName = product_name
#         product.productDesc = product_desc
#         product.productCategory = product_category
#         product.productPrice = product_price
#         product.productStock = product_stock
        
#         if len(request.FILES) != 0:
#             product.productPhoto = request.FILES['productPhoto']
        
#         fss = FileSystemStorage()
        
#         product.save()
        
#         return redirect('marketplace:MyMarketplace')
#     else:
#         return render(request, 'UpdateProduct.html', {'product':product})

def updateProduct(request, fk1):
    product = get_object_or_404(prodProduct, pk=fk1)
    person=Person.objects.get(Email=request.session['Email'])
    stock = get_object_or_404(prodStock, product=product)
    
    if request.method == 'POST':
        productform = ProductForm(request.POST, request.FILES, instance=product)
        stockform = ProductStockForm(request.POST, instance=stock)
        
        if productform.is_valid() and stockform.is_valid():
            updated_product = productform.save(commit=False)
            
            # Custom validation for product name
            if len(updated_product.productName) > 30:
                messages.error(request, 'Product name cannot be more than 30 characters.')
                return redirect(request.META.get('HTTP_REFERER'))

            # Custom validation for product description
            if len(updated_product.productDesc) > 500:
                messages.error(request, 'Product description cannot be more than 500 characters.')
                return redirect(request.META.get('HTTP_REFERER'))

            # Custom validation for product category
            if updated_product.productCategory == "None Selected":
                messages.error(request, 'Product category has to be selected')
                return redirect(request.META.get('HTTP_REFERER'))

            customCategory = request.POST.get('customCategory')
            if updated_product.productCategory == "Others" and customCategory:
                updated_product.productCategory = customCategory

            # Custom validation for product price
            product_price = str(updated_product.productPrice)
            price_pattern = r'^\d+(\.\d{1,2})?$'
            if not re.match(price_pattern, product_price):
                messages.error(request, 'Product price should only contain digits and allow up to two digits after the decimal point.')
                return redirect(request.META.get('HTTP_REFERER'))

            updated_product.save()

            # Save stock form with the saved product instance
            updated_stock = stockform.save(commit=False)
            updated_stock.product = updated_product

            # Custom validation for product stock
            if not str(updated_stock.stock).isdigit():
                messages.error(request, 'Product stock should only contain digits.')
                return redirect(request.META.get('HTTP_REFERER'))

            updated_stock.save()

            messages.success(request, 'Product has been updated successfully.')
            return redirect('marketplace:viewSeller', pk=person.id)
        else:
            # Display form errors
            for field, errors in productform.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

            for field, errors in stockform.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    else:
        productform = ProductForm(instance=product)
        stockform = ProductStockForm(instance=stock)
    
    return render(request, 'ProductForm.html', {'productform': productform, 'stockform': stockform, 'update': True, 'product': product, 'stock': stock, 'person': person})
    
def buy_now(request, fk1,fk2):
    product = prodProduct.objects.get(pk=fk1)
    user = Person.objects.get(pk=fk2)
    if request.method=='POST':
        productqty= int(request.POST.get('productqty'))
        basket = Basket.objects.filter(productid=product,Person_fk=user,is_checkout=0)

        if product.productStock < productqty:
            messages.error(request, f'{product.productName}(s) exceeds the stock limit in your basket')
            return redirect('../../../MainMarketplace.html')

        if len(basket) == 0 : 
            basket = Basket(productqty=productqty,productid=product,Person_fk=user,is_checkout=0,transaction_code='').save()
        else :
            basket = Basket.objects.get(Person_fk=user,productid=product,is_checkout=0)
            if basket.productqty + productqty > product.productStock:
                messages.error(request, f'{product.productName}(s) exceeds the stock limit in your basket')
                return redirect('../../../MainMarketplace.html')
            basket.productqty += productqty
            basket.save()
        
        messages.success(request,'Item successfully added to your basket')
        return redirect('basket:summary')
    return render(request, 'summary.html', {'basket': basket})


def add_to_basket(request, fk1,fk2):
    
    product = prodProduct.objects.get(pk=fk1)
    user = Person.objects.get(pk=fk2)
    if request.method=='POST':
        productqty= int(request.POST.get('productqty'))
        basket = Basket.objects.filter(productid=product,Person_fk=user,is_checkout=0)

        if product.productStock < productqty:
            messages.error(request, f'{product.productName}(s) exceeds the stock limit in your basket')
            return redirect('../../../MainMarketplace.html')

        if len(basket) == 0 : 
            basket = Basket(productqty=productqty,productid=product,Person_fk=user,is_checkout=0,transaction_code='').save()
        else :
            basket = Basket.objects.get(Person_fk=user,productid=product,is_checkout=0)
            if basket.productqty + productqty > product.productStock:
                messages.error(request, f'{product.productName}(s) exceeds the stock limit in your basket')
                return redirect('../../../MainMarketplace.html')
            basket.productqty += productqty
            basket.save()
        
        messages.success(request,'Item successfully added to your basket')
        return redirect('marketplace:MainMarketplace')
    return render(request, '../../../MainMarketplace.html', {'basket': basket})