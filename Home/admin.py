from django.contrib import admin
from .models import CustomUser, Service, HouseworkerProfile, UniqueProfileModel

admin.site.site_header = "ServeSync Admin Portal"
admin.site.site_title = "ServeSync Admin"
admin.site.index_title = "Welcome to ServeSync Administration"


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role']
    search_fields = ['username', 'email']
    list_filter = ['role']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'user', 'created_at']
    search_fields = ['service_name']
    list_filter = ['created_at']

    def user(self, obj):
        return obj.user.username

    user.admin_order_field = 'user__username'

    def created_at(self, obj):
        return obj.created_at

    created_at.admin_order_field = 'created_at'


@admin.register(HouseworkerProfile)
class HouseworkerProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'service', 'contact', 'rating']
    search_fields = ['name', 'service__service_name']
    list_filter = ['service']

admin.site.register(UniqueProfileModel)

