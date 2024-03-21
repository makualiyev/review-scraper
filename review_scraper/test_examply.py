import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://www.ozon.ru/")
    expect(page).to_have_title(re.compile('Обновить'))
    page.get_by_role("button", name="Обновить").click()

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Варочная панель газовая DELVENTO V30H20J001 / 30 см / Газ-контроль / WOK-конфорка / Материал панели закалённое стекло / фронтальная панель управления / safety решетка / жиклеры для баллонного газа / полный комплект / 3 года гарантии"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()