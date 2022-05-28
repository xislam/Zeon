from django.contrib import admin

from career.models import Career
from career.models import Category
from career.models import Country

# Register your models here.

admin.site.register(Career)
admin.site.register(Country)
admin.site.register(Category)
