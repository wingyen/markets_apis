from django.contrib import admin
from orders.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'isin', 'limit_price', 'side', 'valid_until', 'quantity']

admin.site.register(Order, OrderAdmin)
