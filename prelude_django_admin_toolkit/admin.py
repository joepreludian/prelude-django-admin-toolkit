from django.contrib import admin
from django.conf import settings

from prelude_django_admin_toolkit.customizer import PreludeAdminCustomizer
from prelude_django_admin_toolkit.forms import PrlModelForm


# Defining the PRLModelAdmin
class PrlModelAdmin(admin.ModelAdmin):
    form = PrlModelForm


class PrlAdmin(admin.AdminSite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Custom settings Dict
        custom_settings = getattr(settings, 'PRELUDE_ADMIN', None)
       
        # If you haven't set a custom settings, create one
        if custom_settings is None:
            custom_settings = {
                'customizer_object': PreludeAdminCustomizer()
            }
            
        self.prl_customizer = custom_settings['customizer_object']
        
        self.load_customizer()
    
    def load_customizer(self):
        self.site_header = self.prl_customizer.site_header
    
    def each_context(self, request):
        context_vars = super().each_context(request)
       
        context_vars.update(self.prl_customizer.get_context_vars())
 
        return context_vars
     
    def get_urls(self):
        
        url_patterns = super().get_urls()
        
        return url_patterns


site = PrlAdmin()

from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

site.register(User, UserAdmin)
site.register(Group, GroupAdmin)
