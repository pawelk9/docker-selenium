from behave import given, when, then
from pages.login import loginPage
from pages.dashboard import dashboardPage


@when(u'I type "{email}" in email')
def step_impl_email(context, email):
    loginPage.type_email(email)


@when(u'I type "{password}" in password')
def step_impl_password(context, password):
    loginPage.type_password(password)


@when(u'I click log in')
def step_impl_password(context):
    loginPage.click_login()


@then(u'I should be logged in')
def step_impl_logged_in(context):
    dashboardPage.verify_logged_in()


@then(u'Error is displayed')
def step_impl_logged_in(context):
    loginPage.login_error_displayed()
