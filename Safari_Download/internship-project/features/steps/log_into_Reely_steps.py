from behave import *

use_step_matcher("re")


@given("that the user has logged into https://soft\.reelly\.io/off-plan")
def step_impl(context):
    raise NotImplementedError(u'STEP: Given that the user has logged into https://soft.reelly.io/off-plan')


@when("the user clicks Bali")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user clicks Bali')


@then("properties in Bali which are in the system appear")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then properties in Bali which are in the system appear')


@when("the user chooses construction date of 4Q 2024")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user chooses construction date of 4Q 2024')


@then("properties that will have been completed prior to 4Q 2024 will appear")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then properties that will have been completed prior to 4Q 2024 will appear')


@when("the user selects value ranges from 600000 AED to 1\.5 million AED")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user selects value ranges from 600000 AED to 1.5 million AED')


@then("properties in Bali within that value range will appear")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then properties in Bali within that value range will appear')


@when("the user selects property type of 'Apartment'")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user selects property type of \'Apartment\'')


@then("apartments will appear")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then apartments will appear')


@when("the user chooses 'Penthouse'")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user chooses \'Penthouse\'')


@then("penthouses will appear")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then penthouses will appear')