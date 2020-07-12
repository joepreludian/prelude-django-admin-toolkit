from behave import given

from django.contrib.auth.models import User


@given('an authenticated user')
def given_auth_user(context):
    User.objects.create_superuser(username='test', email='foo@bar', password='test')

    br = context.browser

    br.visit(context.base_url + '/admin/')
    br.fill('username', 'test')
    br.fill('password', 'test')
    br.find_by_id('prl-btn-login').first.click()


@given('an unauthenticated user')
def given_auth_user(context):

    br = context.browser

    br.visit(context.base_url + '/admin/')
    br.fill('username', 'invalid_user')
    br.fill('password', 'invalid_password')
    br.find_by_id('prl-btn-login').first.click()
