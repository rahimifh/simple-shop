from django.contrib import admin
from .models import Todo,stuff,order,userdetail
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    readonly_fields=('created',)
admin.site.register(Todo,TodoAdmin)
admin.site.register(stuff)
admin.site.register(order)
admin.site.register(userdetail)
