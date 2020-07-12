from behave import when, then


@when('I access the admin home page')
def when_access_homepage(context):
    br = context.browser
    br.visit(context.base_url + '/admin')

@then('I see the project name on title')
def then_I_see_project_name(context):
    br = context.browser
    body = br.find_by_id('uk-h1')

    assert 'Prl Admin' in body.text

@then('I see the fields of login and password')
def then_I_see_login_password_fields(context):
    br = context.browser

    br.fill('username','something')
    br.fill('password', 'something')

@then('I see my username printed')
def then_I_see_info(context):
    br = context.browser

    body = br.find_by_css('.prl-welcome-msg')

    assert 'Welcome, test' in body.text
