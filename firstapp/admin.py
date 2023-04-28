from django.contrib import admin
from firstapp.models import Theme, Profile
from django.contrib.auth.models import User, Group
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
# Register your models here.
admin.site.register(Profile)
admin.site.unregister(Group)
admin.site.unregister(User)

class ThemeList(ImportExportModelAdmin):
    list_display = ('user','color',)
    list_filter = ('user','color',)

admin.site.register(Theme, ThemeList)

class GroupAdminWithCount(GroupAdmin, ImportExportModelAdmin):
    def user_count(self, obj):
        return obj.user_set.count()

    list_display = GroupAdmin.list_display + ('user_count',)
    
admin.site.register(Group, GroupAdminWithCount)

class UserList(UserAdmin, ImportExportModelAdmin):
    list_display = ('username','email','is_active','date_joined')
    list_filter = ('username','is_superuser','is_staff','is_active','email','date_joined','groups')

admin.site.register(User, UserList)

# Add import export model mixin to the model while registering the model in admin.py
# Example:
# admin.site.register(Theme, ImportExportModelAdmin)

# If you want to list display and list filter the example is below.

# class ThemeList(ImportExportModelAdmin):
#     list_display = ('user','color',)
#     list_filter = ('user','color',)

# admin.site.register(Theme, ThemeList)