from django.test import TestCase, RequestFactory
from prelude_django_admin_toolkit.customizer import PreludeAdminCustomizer
from prelude_django_admin_toolkit.admin import PrlModelAdmin, site
from demoapp.models import Item


class PreludeAdminTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('/', {'user': 'Jonhnatha Trigueiro'})

    def test_instantiate_prl_model_admin(self):
        prl_model_admin = PrlModelAdmin(model=Item, admin_site=site)

        self.assertTrue(prl_model_admin.save_as)
        self.assertEqual(prl_model_admin.list_per_page, 50)