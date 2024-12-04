from playwright.sync_api import expect

RESULT_PREMIUM = '.css-hqbmxg.e18vbajn0'
RESULT_MAZDA = '.ftldj64.css-uewl2b'
class SimpleDrom:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto('https://www.drom.ru/')

    def check_button_mazda_exists(self):
        button = self.page.get_by_role('link', name='Mazda')
        expect(button).to_be_visible()

    def check_button_premium_exists(self):
        button = self.page.get_by_role('link', name='Премиум')
        expect(button).to_be_visible()

    def click_button_premium(self):
        button = self.page.get_by_role('link', name='Премиум')
        button.click()

    def click_button_mazda(self):
        button = self.page.get_by_role('link', name='Mazda')
        button.click()

    def check_premium_result_text_is_(self, text):
        result = self.page.locator(RESULT_PREMIUM)
        expect(result).to_have_text(text)

    def check_mazda_result_text_is_(self, text):
        result = self.page.locator(RESULT_MAZDA)
        expect(result).to_have_text(text)