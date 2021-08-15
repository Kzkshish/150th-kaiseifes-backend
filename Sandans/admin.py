# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Sandans.models import Sandan, OnlineSandan


class SandanAdmin(UserAdmin):
    model = Sandan
    fieldsets = UserAdmin.fieldsets + \
        ((None, {'fields': ('icon', 'waittime',)}),)
    list_display = ["username"]


admin.site.register(Sandan, SandanAdmin)
admin.site.register(OnlineSandan)
