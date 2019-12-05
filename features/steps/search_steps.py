from behave import given, when, then

"""  Given Tap on search field
    When Enter Python to search field
    Then Top result for Python is shown"""


@given('Tap on search field')
def tap_search(context):
    context.app.launch_page.tap_search()


@when('Enter {search_phrase} to search field')
def input_search(context, search_phrase):
    context.app.search_page.input_search(search_phrase)


@then('Top result for {search_phrase} is shown')
def verify_search_result(context, search_phrase):
    context.app.search_page.verify_search_result(search_phrase)


@then("'{message}' message is shown")
def verify_no_results_message(context, message):
    context.app.search_page.verify_no_results(message)
