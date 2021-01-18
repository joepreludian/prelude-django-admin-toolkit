from prelude_django_admin_toolkit.customizer import PreludeAdminCustomizer, PreludeDefaultIndexPage, DIVIDER
from django.utils.translation import gettext_lazy as _


my_admin = PreludeAdminCustomizer(site_header='MyAdmin')

my_admin.site_css = 'site_default.css'

my_admin.register_menu(
    name=_('Itemization'),
    icon='heart',
    items= [
        {'name': _('Heart Item'), 'icon':'user', 'to': 'demoapp.item'},
        {'name': _('External'), 'icon': 'heart', 'to': 'http://google.com'},
        {'type': DIVIDER },
        {'name': _('External 2'), 'to': 'demoapp.item'},
        {'name': _('External 2'), 'to': 'demoapp.item'}
    ])

my_admin.register_menu(name=_('Project'), icon='user', to='http://terra.com.br')

index = PreludeDefaultIndexPage()

my_admin.configure_index(index = index)