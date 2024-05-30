from django.contrib import admin
from products.models import Category, Product, Order, Contact


admin.site.site_header = "Product_management"
admin.site.site_title = "Hande_products"
admin.site.index_title = "Manager"


class AdminCategory(admin.ModelAdmin):
    list_display = ('name',)


class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'get_category_name','date_creation')
    search_fields = ('name',)
    list_editable = ('price',)

    def get_category_name(self, obj):
        return obj.category.name
    get_category_name.short_description = 'Category'

class AdminOrder(admin.ModelAdmin):
    list_display = ('items','name', 'email', 'city','state','zipcode','date_commande','total')



admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Order, AdminOrder)
admin.site.register(Contact)



