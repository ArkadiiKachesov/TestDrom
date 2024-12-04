from playwright.sync_api import Page
from pages.simple_drom import SimpleDrom

def test_button(page: Page):
    simple_page = SimpleDrom(page)
    simple_page.open()
    simple_page.check_button_premium_exists()

def test_button_click(page: Page):
    simple_page = SimpleDrom(page)
    simple_page.open()
    simple_page.click_button_premium()
    simple_page.check_premium_result_text_is_('Продажа новых автомобилей в Новосибирской области')
