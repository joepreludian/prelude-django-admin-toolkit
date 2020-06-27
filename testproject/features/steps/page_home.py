from behave import when, then


@when('I access the admin home page')
def when_access_homepage(context):
    br = context.browser
    br.visit(context.base_url + '/admin')


@then('I see my username printed')
def then_I_see_info(context):
    br = context.browser

    body = br.find_by_css('.prl-welcome-msg')

    assert 'Welcome, test' in body.text
