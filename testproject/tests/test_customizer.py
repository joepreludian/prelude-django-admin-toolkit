from django.test import TestCase, RequestFactory
from prelude_django_admin_toolkit.customizer import PreludeAdminCustomizer


class PreludeAdminCustomizerTestCase(TestCase):
    
    def setUp(self):
        self.c = PreludeAdminCustomizer(site_header='PreludeAdmin')
        self.factory = RequestFactory()
        self.request = self.factory.get('/', {'user': 'Jonhnatha Trigueiro'})
    
    def test_clean_context(self):
        context_vars = self.c.get_context_vars(self.request)
        
        expected_context_vars = {
            'custom_menu': [],
            'admin': {
                'site_css': 'site_default.css',
                'show_about': True,
                'enable_pwa': True,
                'index': {
                    'template_name': None,
                    'show_apps': False,
                    'context': {}
                }
            }
        }
        
        self.assertEqual(context_vars, expected_context_vars)
    
    def test_add_menu(self):
        self.c.register_menu(name='TmpMenu', items=[
            {'name': 'temp_value'},
        ])

        expected_context_vars = {
            'admin': {
                'site_css': 'site_default.css',
                'show_about': True,
                'enable_pwa': True,
                'index': {
                    'template_name': None,
                    'show_apps': False,
                    'context': {}
                }
            },
            'custom_menu': [
                {'name': 'TmpMenu', 
                 'to': None,
                 'icon': None,
                 'items': [
                    {'name': 'temp_value',
                     'icon': None, 
                     'to': None,
                     'type': 'item'}
                ]}
            ]}

        self.assertEqual(self.c.get_context_vars(self.request),
                         expected_context_vars)
    
    def test_single_menu_entry(self):
        """Test if menu will work if added a simple entry"""
        
        self.c.register_menu('SingleMenu', to='http://tempurl', icon='house')
        
        context = self.c.get_context_vars(self.request)
        single_menu = context['custom_menu'][0]
        
        print(single_menu)
        
        self.assertEqual(single_menu['name'], 'SingleMenu')
        self.assertEqual(single_menu['to'], 'http://tempurl')
        self.assertEqual(single_menu['icon'], 'house')
   
    def test_detect_divider(self):
        self.c.register_menu('SingleHR', items=[{'type': 'divider'}])

        context = self.c.get_context_vars(self.request)
        
        menu = context['custom_menu'][0]
        print(menu['items'][0])
        
        self.assertEqual(menu['name'], 'SingleHR')
        self.assertTrue('type' in menu['items'][0].keys())
        
        self.assertEqual(menu['items'][0]['type'], 'divider')

    def test_override_site_css(self):
        
        self.c.site_css = 'another_site_default.css'
        
        context = self.c.get_context_vars(self.request)
        
        self.assertEqual(context['admin']['site_css'], 'another_site_default.css')