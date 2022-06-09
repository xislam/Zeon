from django.contrib import admin

from career.models import Career
from career.models import Country
from career.models import CV
from career.models import Direction
from career.models import Status

# Register your models here.

admin.site.register(Career)
admin.site.register(Country)
admin.site.register(Direction)
admin.site.register(CV)
admin.site.register(Status)
