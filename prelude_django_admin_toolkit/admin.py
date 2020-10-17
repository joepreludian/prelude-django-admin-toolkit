from django.contrib import admin
from django.contrib.admin.sites import site
from django.conf import settings

from .forms import PrlModelForm


class PrlModelAdmin(admin.ModelAdmin):
    form = PrlModelForm


# This class belongs to prelude_django_admin_toolkit
class PrlAdmin(admin.AdminSite):
    #site_header = 'TEST'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Custom settings class
        custom_settings = getattr(settings, 'PRELUDE_ADMIN', None)
        if custom_settings is not None:
            custom_admin = custom_settings.get('customizer_object', None)
            if custom_admin is not None:
                self.site_header = custom_admin.site_header

site = PrlAdmin()

from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

site.register(User, UserAdmin)
site.register(Group, GroupAdmin)
