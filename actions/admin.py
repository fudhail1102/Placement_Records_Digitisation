from django.contrib import admin
from django.contrib import messages
from .models import Permission
from django.utils import timezone 
# Register your models here.
class PermissionAdmin(admin.ModelAdmin):
    readonly_fields = ('requested_time', 'acknowledged_time', 'staff', 'reason', 'status')
    list_display = ['staff', 'reason', 'status']
    actions = ['accept_permissions', 'reject_permissions']
    
    def accept_permissions(self, request, queryset):
        queryset.update(status = 'A', acknowledged_time = timezone.now())
        messages.success(request, "The requests have been accepted.")
    def reject_permissions(self, request, queryset):
        queryset.delete()
        messages.error(request, "The requests have been rejected.")


admin.site.register(Permission, PermissionAdmin)
