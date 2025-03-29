from django.contrib import admin
from .models import Category, Product,Cart,CartItem,Order,OrderItem

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','created_by']
    search_fields = ['name']
    ordering = ['name']
    list_per_page = 10
    
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','category','created_by','stock_quantity','created_date']
    search_fields = ['name','category']
    ordering = ['name','price','category']
    list_per_page =10
    
admin.site.register(Product, ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ['user','updated_at','created_at']
    search_fields = ['user']
    ordering = ['user', 'created_at']
    list_per_page =10
    
admin.site.register(Cart, CartAdmin)
class CartItemAdmin(admin.ModelAdmin):
    list_display =['cart','product','quantity']
    search_fields =['cart','product']
    ordering =['cart','product']
    list_per_page = 10
admin.site.register(CartItem, CartItemAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at','status','total_amount']
    search_fields = ['user','status','total_amount']
    ordering = ['user','created_at','status']
    list_per_page = 10
admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order','product','quantity']
    search_fields =['order','product']
    ordering = ['order','product']
    list_per_page = 10
admin.site.register(OrderItem,OrderItemAdmin)
