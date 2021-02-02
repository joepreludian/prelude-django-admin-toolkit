from prelude_django_admin_toolkit.customizer import PreludeAdminCustomizer, PreludeDefaultIndexPage, DIVIDER
from django.utils.translation import gettext_lazy as _


my_admin = PreludeAdminCustomizer(site_header='SiteProject', site_title='Site Title')

my_admin.site_css = 'site_default.css'

my_admin.register_menu(
    name=_('Subscribers'),
    icon='social',
    items= [
        {'name': _('Patrons'), 'icon':'user', 'to': 'demoapp.item'},
        {'name': _('Favorites'), 'icon': 'heart', 'to': 'http://google.com'},
        {'type': DIVIDER },
        {'name': _('Dummy Text 1'), 'to': 'demoapp.item'},
        {'name': _('Dummy Text 2'), 'to': 'demoapp.item'}
    ])

my_admin.register_menu(name=_('Project'), icon='user', to='http://terra.com.br')
my_admin.register_menu(name=_('Test'), icon='star', to='http://terra.com.br')

index = PreludeDefaultIndexPage()

my_admin.configure_index(index = index)
