from playwright.sync_api import Page
from pages.simple_drom import SimpleDrom

def test_button(page: Page):
    simple_page = SimpleDrom(page)
    simple_page.open()
    simple_page.check_button_mazda_exists()

def test_button(page: Page):
    simple_page = SimpleDrom(page)
    simple_page.open()
    simple_page.click_button_mazda()
    simple_page.check_mazda_result_text_is_('Продажа Mazda')

