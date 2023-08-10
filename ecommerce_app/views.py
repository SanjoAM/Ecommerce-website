from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from cart.cart import Cart
import datetime
import random

# Create your views here.
def home(request):
    products = ProductModel.objects.all()
    category = CategoryModel.objects.all()
    return render(request, 'home.html', {'products': products ,'category':category})





def signin_page(request):
    return render (request,'signin.html')


def signup_page(request):
    return render(request,'signup.html')


def admin_home(request):
    return render(request,'admin.html')



    




def create_customer(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']	
        email = request.POST['email']
        username   = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        cus_address = request.POST['cus_address']
        cus_phone = request.POST['cus_phone']

        image= request.FILES.get('file')


        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'this username Already Exist')
                return redirect('signup_page')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'this email already Exist')
                return redirect('signup_page')
            
            else:
                user = User.objects.create_user(first_name=first_name,
                                                last_name=last_name,
                                                email=email,
                                                username=username,
                                                password=password,)
                user.save()

                data = User.objects.get(id=user.id)
                cus_data =CustomerModel(cus_address=cus_address,
                                        cus_phone=cus_phone,
                                        cus_image=image,
                                        cus_name=data)  
                cus_data.save()
                messages.success(request,'welcome '+data.first_name)
        else:
            messages.info(request,'Password does not Match')
        return redirect('home')  # Replace 'home' with the URL name of the page you want to redirect to
    else:
        return render(request, 'signin_page.html')   


def user_login(request):
    if request.method == 'POST':
        try:


            username = request.POST['username'] 
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                 if user.is_staff:
                     
                     auth.login(request,user)
                     return redirect('product_list')
                 else:
            
           
                     auth.login(request,user)
                     messages.info(request, f'thank you {username}')
                     return redirect('customer_home')  
            else:
               
                messages.info(request, 'Invalid username or password')
                return render('signup_page')
              
        except:
            messages.info(request, 'Invalid username or password')
            
            return redirect('signup_page')   
    return render('signup_page')  
        

def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect('home')        




def addproduct_page(request):
    categories =CategoryModel.objects.all()
    return render(request,'admin_addproduct.html', {'categories': categories})


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        prd_description = request.POST['prd_description']
        image = request.FILES.get('image')
        price = request.POST.get('price')
        category = request.POST['category']  # Assuming you have a select field in the form with name="category"

        # Get the selected category object
        category = CategoryModel.objects.get(pk=category)

        # Create the product object and save it to the database
        product = ProductModel(name=name,
                               prd_description=prd_description,
                               image=image,
                               price=price,
                               category=category)

        product.save()
        return redirect('admin_home')  # Redirect to the admin home page after adding the product
    else:
        # Fetch all available categories to pass to the template
        categories = CategoryModel.objects.all()
        return render(request, 'add_product.html', {'categories': categories})  # Rende


def product_list(request):
    products = ProductModel.objects.all()
    return render(request, 'admin_productlist.html', {'products': products})


def editproduct_page(request ,product_id):
    product = ProductModel.objects.get(id=product_id)
    return render(request, 'admin_editproduct.html', {'product': product})



def edit_product(request, product_id):
    product = get_object_or_404(ProductModel, id=product_id)
    if request.method == 'POST':
        # Process form data and update the product
        product.name = request.POST['prd_name']
        product.prd_description = request.POST['prd_description']
        product.price = request.POST["prd_price"]
        product_oldImage=product.image
        product_newImage=request.FILES.get('image')
        if product_oldImage!=None and product_newImage==None:
            product.image=product_oldImage
        else:
            product.image=product_newImage
        product.save()
        return redirect('product_list')
    return render('product_list')

def delete_product(request, product_id):
    product = get_object_or_404(ProductModel, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request,'productlist.html', {'product': product})



def add_category(request):
    if request.method == 'POST':
        cat_name = request.POST['cat_name']

        # Create the category object and save it to the database
        category = CategoryModel(cat_name=cat_name)
        category.save()

        return redirect('admin_home')  # Redirect to the admin home page after adding the category
    else:
        return render(request, 'add_category.html')  # Render the template for adding the category form







def signin(request):

  
   messages.info(request, 'Please login to add items to the cart.')
   return redirect('home')


@login_required
def customer_home(request):
      

            products= ProductModel.objects.all()
            category = CategoryModel.objects.all()
            cart = CartModel.objects.all()

        
     
            return render(request, 'customer.html', { 'products': products, 'category': category , 'cart':cart})

        #=====================--------CART--------================
"""
def add_tocart (request,id):
   if request.method=='POST':

        
        product = ProductModel.objects.get(id=id)
        print(product)
        cuser=request.user.id
        customer = CustomerModel.objects.get(cus_name=cuser)
        quantity=request.POST['quantity']
        
        cart = CartModel(product=product,customer=customer,quantity=quantity)
        cart.save()



    return redirect('customer_home')  """

"""def cart_page(request):
    return render(request,'customer_cart.html')"""


@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = ProductModel.objects.get(id=id)

    cart.add(product=product)
    return redirect("customer_home")


"""@login_required(login_url='signin_page')
def cart_page(request,cid):
    cuser=request.user.id
    user=CustomerModel.objects.get(id=cuser)
    print(user)
    category=CategoryModel.objects.all()
    product=ProductModel.objects.get(id=cid)
    cart_items = CartModel.objects.filter(customer_id=cid)
    print(cart_items)
    return render(request,'customer_cart.html',{'cart_items':cart_items,'category':category,'product':product})

    """

def item_clear(request, id):
    cart = Cart(request)
    product = ProductModel.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


def item_increment(request, id):
    cart = Cart(request)
    product = ProductModel.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")



def item_decrement(request, id):
    cart = Cart(request)
    product = ProductModel.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")
    


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")    


@login_required()
def cart_detail(request):
    return render(request, 'cart_detail.html')




"""def remove_cart(request,crid):
    cart=CartModel.objects.get(id=crid)
    cid=request.user.id
    cart.delete()
    return redirect('customer_home')"""



def categorywise(request ,cid):
   # category = CategoryModel.objects.all()
    category =CategoryModel.objects.get(id=cid)
    products= ProductModel.objects.filter(category=category)

    return render(request, 'categorywise.html' ,{'category':category , 'products':products})


def confirmation(request):
    return render(request,'create_order.html')

"""@login_required(login_url='signin_page')
def create_order(request):
    if request.method == 'POST':
        customer = CustomerModel.objects.get(cus_name=request.user)
        order_number = generate_order_number()  # You can implement your own logic for generating order numbers
       # Implement your own logic to calculate total amount
        shipping_address = request.POST['shipping_address']
        payment_method = request.POST['payment_method']
        product = ProductModel.objects.get(name=product.name)
        order = OrderModel(
            order_number=order_number,
            customer=customer,
            product=product,
           
            shipping_address=shipping_address,
            payment_method=payment_method
        )
        order.save()
        return redirect('order_list')
    return render(request, 'create_order.html')"""




"""@login_required(login_url='signin_page')
def create_order(request):
    if request.method == 'POST':
        customer = CustomerModel.objects.get(cus_name=request.user)
        order_number = generate_order_number()  # You can implement your own logic for generating order numbers
        
        # Retrieve product details from cart
        cart_items = request.session.Cart
        product_ids = [key for key, _ in cart_items]
        products = ProductModel.objects.filter(id__in=product_ids)
        
        product_name=  ProductModel.objects.filter(name__in=product_ids)
        shipping_address = request.POST['shipping_address']
        
        
        order = OrderModel.objects.create(
            order_number=order_number,
            customer=customer,
            products = products,
            product_name=product_name,
            shipping_address=shipping_address,
         
            # Other order fields
        )
        
        # Associate products with the order
        for product_id, cart_item in cart_items.items():
            product = products.get(id=product_id)
            order.products.add(product)
            
        # Clear the cart
        del request.session['cart']
        
        return redirect('order_confirmation_page')  # Redirect to order confirmation page
    
    return render(request, 'confirmation.html')"""




@login_required(login_url='signin_page')
def create_order(request):
  if request.method == 'POST':
       order_number = generate_order_number()
       customer = CustomerModel.objects.get(cus_name=request.user)
       contact_number =customer.cus_phone
       product_name=request.POST['product_name']
       total_amount=request.POST['total_amount']
       payment_method=request.POST['payment_method']


       order = OrderModel(
           order_number = order_number,
           customer=customer,
           contact_number=contact_number,
           product_name= product_name,
           total_amount =total_amount,
           payment_method = payment_method
           )    
       order.save()
       cart = Cart(request)
       cart.clear()

       return redirect('customer_home')
  return render(request ,'cart_details.html')  
      


def generate_order_number():
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    # Generate a random 4-digit number
    random_number = ''.join([str(random.randint(0, 9)) for _ in range(4)])

    # Combine timestamp and random number to create the order number
    order_number = f'{timestamp}{random_number}'
    return order_number




def orders(request):
    orders=OrderModel.objects.all()
    return render(request,'admin_orderlist.html', {'orders':orders})



@login_required
def custcat(request ,cid):
    category =CategoryModel.objects.get(id=cid)
    products= ProductModel.objects.filter(category=category)

    return render(request, 'categorywise.html' ,{'category':category , 'products':products})

