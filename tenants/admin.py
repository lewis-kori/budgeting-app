from django.contrib import admin

from .models import Department, Tenant


# extend the django model admin for the tenant model
class TenantAdmin(admin.ModelAdmin):
    search_fields = ('name','business_email',)
    list_display = ('name','business_email', 'is_active',)

# Register your models here.
admin.site.register(Department)
admin.site.register(Tenant, TenantAdmin)
