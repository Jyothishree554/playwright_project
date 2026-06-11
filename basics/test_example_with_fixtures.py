import re
from playwright.sync_api import Page,expect
import pytest

@pytest.fixture(scope="function",autouse=True)
def before_each_after_each(page:Page):
    print("before the test run")
    page.goto("https://playwright.dev/")
    yield
    print("after the test run")

def test_main_navigation(page:Page):
    expect(page).to_have_url("https://playwright.dev/")