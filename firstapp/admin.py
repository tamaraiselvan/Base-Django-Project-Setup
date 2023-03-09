from django.contrib import admin
from firstapp.models import Theme, Profile
from django.contrib.auth.models import User, Group
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.unregister(User)
admin.site.register(User, ImportExportModelAdmin)
admin.site.unregister(Group)
admin.site.register(Group, ImportExportModelAdmin)
admin.site.register(Theme)
admin.site.register(Profile)