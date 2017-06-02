from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    '''
        Tabular Inline View for OrderItem
    '''
    model = OrderItem
    raw_id_fields = ('product',)


class OrderAdmin(admin.ModelAdmin):
    '''
        Admin View for Order
    '''
    list_display = ('id', 'first_name', 'last_name', 'email', 'address',
                    'postal_code', 'city', 'paid')
    list_filter = ('paid', 'created', 'updated')
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
