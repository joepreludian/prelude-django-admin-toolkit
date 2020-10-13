from django.contrib import admin
from django.contrib.admin.sites import site
from .forms import PrlModelForm


class PrlModelAdmin(admin.ModelAdmin):
    form = PrlModelForm


class PrlAdmin(admin.AdminSite):
    site_header = 'TEST'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


site = PrlAdmin()

from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

site.register(User, UserAdmin)
site.register(Group, GroupAdmin)
