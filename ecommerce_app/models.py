from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CategoryModel(models.Model):
    cat_name=models.CharField(max_length=70)



class CustomerModel(models.Model):
    cus_name=models.ForeignKey(User,on_delete=models.CASCADE,null=True , related_name='customer_model')
    cus_email=models.EmailField
    cus_address=models.CharField(max_length=70)
    cus_phone=models.CharField(max_length=70)
    cus_image=models.ImageField(upload_to="image/",null=True)

class ProductModel(models.Model):
    name=models.CharField(max_length=70,null=True)
    prd_description=models.CharField(max_length=70)
    image = models.ImageField(upload_to="products/",null=True)
    prd_addate=models.DateField(auto_now_add=True,null=True)
    price=models.FloatField(max_length=70,null=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True, related_name='products')



"""cart_item.name
cart_item.price
cart_item.quantity
"""
class CartModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE,max_length=70,null=True)
    product_name =models.CharField(max_length=70,null=True) 
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE,max_length=70,null=True)
    quantity = models.FloatField( max_length=70,default=0)  # You can add more fields related to the cart, such as quantity
    total_price = models.FloatField(max_length=70,null=True) 
    # Optionally, you can also add a field for the date and time when the item was added to the cart.
    added_at = models.DateTimeField(auto_now_add=True)


    
 


class OrderModel(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(ProductModel , on_delete=models.CASCADE , null=True)
    product_name =models.CharField(max_length=70,null=True) 
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=20, default='Processing')
    shipping_address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Order {self.order_number} - {self.customer.cus_name}"



