from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Product, Category
from django.utils.safestring import mark_safe


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','content','get_photo','price','in_stock','is_published','created','update','category')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content', 'price')
    readonly_fields = ('get_photo', 'created', 'update')
    list_editable = ('is_published', 'in_stock')

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" width="75">')
    get_photo.short_description = 'Картинка'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','get_photo','name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" width="75">')
    get_photo.short_description = 'Картинка'


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Панель керування магазином'
admin.site.site_header = 'Панель керування магазином'