from api.models import Ceo
from django.contrib import admin

# Register your models here.

class AdminCeo(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'ceo', 'since']

admin.site.register(Ceo, AdminCeo)