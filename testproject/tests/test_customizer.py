from django.test import TestCase
from prelude_django_admin_toolkit.customizer import PreludeAdminCustomizer


class PreludeAdminCustomizerTestCase(TestCase):
    
    def setUp(self):
        self.c = PreludeAdminCustomizer(site_header='PreludeAdmin')
        
    
    def test_clean_context(self):
        context_vars = self.c.get_context_vars()
        
        expected_context_vars = {
            'custom_menu': []
        }
        
        self.assertEqual(context_vars, expected_context_vars)
    
    def test_add_menu(self):
        self.c.register_menu(name='TmpMenu', items=[
            {'name': 'temp_value'},
        ])

        expected_context_vars = {
            'custom_menu': [
                {'name': 'TmpMenu', 
                 'to': None,
                 'icon': None,
                 'items': [
                    {'name': 'temp_value',
                     'icon': None, 
                     'to': None}
                ]}
            ]}

        self.assertEqual(self.c.get_context_vars(),
                         expected_context_vars)
    
    def test_single_menu_entry(self):
        """Test if menu will work if added a simple entry"""
        
        self.c.register_menu('SingleMenu', to='http://tempurl', icon='house')
        
        context = self.c.get_context_vars()
        single_menu = context['custom_menu'][0]
        
        print(single_menu)
        
        self.assertEqual(single_menu['name'], 'SingleMenu')
        self.assertEqual(single_menu['to'], 'http://tempurl')
        self.assertEqual(single_menu['icon'], 'house')
    