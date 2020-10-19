from prelude_django_admin_toolkit.customizer import PreludeAdminCustomizer
from django.utils.translation import gettext_lazy as _


my_admin = PreludeAdminCustomizer(site_header='MyAdmin')

my_admin.register_menu(
    name=_('Authorization'),
    items= [
        {'name': _('Item'), 'icon':'heart', 'to': 'demoapp.item'},
        {'name': _('External'), 'to': 'http://google.com'},
        {'name': _('External 2'), 'to': 'demoapp.item'}
    ])

my_admin.register_menu(name=_('Project'), icon='user', to='http://terra.com.br')