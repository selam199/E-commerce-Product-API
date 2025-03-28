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
    
admin.site.register(Product, ProductAdmin)




admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
