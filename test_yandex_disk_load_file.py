from time import sleep

from conftest import *
from pages.base_page import BasePage


def test_yandex_disk_load_file(browser):
    """ Перед выполнением теста лучше выключить VPN (если он включен). В тесте нет проверки на "робота"! """

    base_page = BasePage(browser)
    login = 'enot-2023'
    password = 'Enot_2023_2023'
    name_text_file = 'sample.txt'
    path = rf"c:\Tests\{name_text_file}"

    try:
        base_page.open()
        base_page.login_to_yandex(login, password)
        base_page.go_to_disk()
        name_folder = base_page.generate_unique_folder_name()
        base_page.create_folder(name_folder)
        base_page.find_and_open_folder(name_folder)
        base_page.upload_file_txt(path)
        base_page.find_and_open_file(name_text_file)
        sleep(5)
        expected_text = base_page.read_text_from_file(path).strip()
        text_from_site = base_page.check_text_uploaded_file()
        assert text_from_site == expected_text, "Ошибка: Текст в файле не соответствует ожиданиям"
        base_page.close_uploaded_file(name_text_file)
        base_page.logout()

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        browser.quit()