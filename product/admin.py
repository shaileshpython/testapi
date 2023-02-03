from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from .models import Product

# Register your models here.


class ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass
    # list_display = ('name', 'title', 'view_birth_date')

admin.site.register(Product, ProductAdmin)
