from django.contrib import admin

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ['name']}
admin.site.register(Product, ProductAdmin)


class ToppingAdmin(admin.ModelAdmin):
    list_display = ['name', 'available']
    list_filter = ['available']
    list_editable = ['available']
admin.site.register(Topping, ToppingAdmin)

class DekorAdmin(admin.ModelAdmin):
    list_display = ['name', 'available']
    list_filter = ['available']
    list_editable = ['available']
admin.site.register(Dekor, DekorAdmin)