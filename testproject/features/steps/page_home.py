from behave import when, then
from testproject.prelude_admin import my_admin


@when('I access the admin home page')
def when_access_homepage(context):
    br = context.browser
    br.visit(context.base_url + '/admin')

@then('I see the project name on title')
def then_I_see_project_name(context):
    br = context.browser
    body = br.find_by_id('uk-h1')

    assert my_admin.site_header in body.text

@then('I see the fields of login and password')
def then_I_see_login_password_fields(context):
    br = context.browser

    br.fill('username','something')
    br.fill('password', 'something')

@then('I see my username printed')
def then_I_see_info(context):
    br = context.browser

    body = br.find_by_css('.prl-username-item')

    print(f'BODY TEXT: {body.text}')
    assert 'TEST' in body.text

@when('I access the logout page')
def when_I_go_to_logout_page(context):
    br = context.browser
    
    br.find_by_css('.prl-username-item').mouse_over()
    

@when('I click on the logout button')
def when_I_click_on_logout_button(context):
    br = context.browser
    
    br.links.find_by_partial_text('Log out').click()