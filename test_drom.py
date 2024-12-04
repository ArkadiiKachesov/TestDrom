from playwright.sync_api import Page, expect

def test_drom(page: Page):
    page.goto('https://www.drom.ru/')
    # Открыли ссылку на дром
    page.get_by_role('link', name='Mazda').click()
    # Нашли кнопку с названием Mazda и кликнули по ней
    expect(page.get_by_text('Продажа Mazda')).to_be_visible()
    # Ожидаемый результат что на открывшейся странице есть текст "Продажа Mazda"

def test_drom2(page: Page):
    page.goto('https://www.drom.ru/')
    page.get_by_role('link', name='Mazda').click()
    page.get_by_role('link', name='Статистика цен Mazda на японских аукционах').click()
    expect(page.get_by_text('Статистика продаж Mazda с аукционов Японии')).to_be_visible()
