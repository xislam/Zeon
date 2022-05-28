from django.contrib import admin

from career.models import Career
from career.models import Country
from career.models import Direction

# Register your models here.

admin.site.register(Career)
admin.site.register(Country)
admin.site.register(Direction)
