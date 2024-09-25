from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "name",
        "is_staff",
        "password",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
    # fieldsets = (('my_name_label', {"fields": ("name", "password")}),)
    add_fieldsets = UserAdmin.add_fieldsets + (('_name_label', {"fields": ("name",)}),)
    # add_fieldsets =  (('my_name_label', {"fields": ("name",)}),)

admin.site.register(CustomUser, CustomUserAdmin)
