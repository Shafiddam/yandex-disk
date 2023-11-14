from time import sleep

from conftest import *
from pages.base_page import BasePage


def test_yandex_disk(browser):
    """ Перед выполнением теста лучше выключить VPN (если он включен). В тесте нет проверки на "робота"! """

    base_page = BasePage(browser)
    login = 'enot-2023'
    password = 'Enot_2023_2023'
    name_folder = 'Folder_1'
    name_text_file = 'File_1'

    try:
        base_page.open()
        base_page.login_to_yandex(login, password)
        base_page.go_to_disk()
        base_page.create_folder(name_folder)
        base_page.find_and_open_folder(name_folder)
        base_page.create_file(name_text_file)
        base_page.close_created_file(name_text_file)
        element = base_page.check_created_file(name_text_file)
        assert element, "Ошибка: файл не был создан!"
        assert (element.get_attribute("aria-label") == f"{name_text_file}.docx"), \
            "Ошибка: название файла не соответствует ожидаемому!"
        sleep(3)
        base_page.logout()

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        browser.quit()


