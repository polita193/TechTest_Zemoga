from behave import *
from pages.home_page import HomePage
from hamcrest import assert_that

CARNIVAL_URL = 'https://www.carnival.com/'


@step('a web browser is in Carnival page')
def step_impl(context):
    page = HomePage(context)
    page.go(CARNIVAL_URL)


@step('I search a cruise to "{sail_to}" with a duration of "{duration}"')
@step('The results of a cruise search to {sail_to} with {duration} duration are shown')
def step_impl(context, sail_to, duration):
    page = HomePage(context)
    page.search_cruise(sail_to, duration)


@step('the results grid is displayed')
def step_impl(context):
    page = HomePage(context)
    assert_that(page.results_grid_is_displayed(), "The results grid isn't displayed")


@step('the filter by price option is controlled by an slider')
def step_impl(context):
    page = HomePage(context)
    assert_that(page.check_filter_by_price(), "The filter by price isn't displayed")


