from ecommerce_app import views
from django.urls import path 

urlpatterns = [
    path('',views.home,name='home'),
    path('signin_page',views.signin_page,name='signin_page'),
    path('signup_page',views.signup_page,name='signup_page'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('addproduct_page',views.addproduct_page,name='addproduct_page'),
    path('editproduct_page/<int:product_id>',views.editproduct_page,name='editproduct_page'),
    path('add_category',views.add_category,name='add_category'),
    path('logout',views.logout,name='logout'),
    path('signin',views.signin,name='signin'),
   # path('remove_cart/<int:crid>',views.remove_cart,name='remove_cart'),
   # path('cart_page/<int:cid>',views.cart_page,name='cart_page'),
   # path('add_tocart/<int:id>',views.add_tocart,name='add_tocart'),
    path('customer_home/<str:user>/', views.customer_home, name='customer_home'),
    path('product_list', views.product_list, name='product_list'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add_product',views.add_product,name='add_product'),
    path('create_customer/',views.create_customer,name='create_customer'),
    path('user_login',views.user_login,name='user_login'),
    path('customer_home',views.customer_home,name='customer_home'),
   # path('cart_page',views.cart_page,name='cart_page'),
    path('categorywise/<int:cid>',views.categorywise,name='categorywise'),
    path('custcat/<int:cid>',views.custcat,name='custcat'),
    path('create_order',views.create_order,name='create_order'),
    path('confirmation',views.confirmation,name='confirmation'),
    path('orders',views.orders,name='orders'),                  
    
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
]