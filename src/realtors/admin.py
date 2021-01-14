from django.contrib import admin
from .models import Realtor
# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Realtor,RealtorAdmin)