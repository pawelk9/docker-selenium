from behave import given, when, then
from framework.webapp import webapp


@given(u'I load the website')
def step_impl_load_website(context):
    webapp.load_website()


@when(u'I go to "{page}" page')
def step_impl_goto_page(context, page):
    webapp.goto_page(page)


@given(u'I go to Login page')
def step_goto_login_page(context):
    webapp.goto_page('tester-account/sign-in')


@then(u'I close the browser')
def step_close_browser(context):
    webapp.close_browser()
