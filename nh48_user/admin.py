from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from nh48_user.models import NHUser

admin.site.register(NHUser, UserAdmin)

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('bio',)}),