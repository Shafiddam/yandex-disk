from time import sleep

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains




class BasePage:
    class Locators:
        BASE_URL = 'https://passport.yandex.ru/auth/welcome'
        DISK_URL = 'https://360.yandex.ru/disk'
        INPUT_FIELD = (By.XPATH, '//input[@id="passp-field-login"]')
        CHECKBOX = (By.XPATH, '//input[@id="js-button"]')
        BTN_GOTO_DISK = (By.XPATH, '//a[@href = "https://disk.yandex.ru"]')
        BTN_DISK = (By.XPATH, '//a[@href="https://360.yandex.ru/disk" and '
                              'contains(@class, "Button2_type_link") and '
                              'contains(@class, "Link_3eWZ3ihlWxFPc7X7WwWfeT") and '
                              'contains(@class, "WithIcon_1t2UrWHXuaDRpdFz2evI-t")]')
        BTN_ENTER_TO_YANDEX = (By.ID, 'passp:sign-in')
        BTN_USER_ACCOUNT = (By.CSS_SELECTOR, '.PSHeader-User.PSHeader-User_noUserName.promozavr-anchor-user')
        BTN_USER_ACCOUNT_LOGOUT = (By.CSS_SELECTOR,
                            '.menu__item.menu__item_type_link.legouser__menu-item.legouser__menu-item_action_exit')
        INPUT_FIELD_PASSWORD = (By.ID, 'passp-field-passwd')
        BTN_CREATE = (By.CSS_SELECTOR, '.Button2.Button2_view_raised.Button2_size_m.Button2_width_max')
        BTN_CREATE_FOLDER = (By.XPATH, '//*[contains(@class,"create-resource-button__text")][text()="Папку"]')
        BTN_CREATE_TEXT_FILE = (By.XPATH, '//*[contains(@class,"create-resource-button__text")]'
                                          '[text()="Текстовый документ"]')
        INPUT_NAME_FOLDER = (By.XPATH, '//input[@class="Textinput-Control" and @value="Новая папка"]')
        INPUT_NAME_TEXT_FILE = (By.XPATH, '//input[@class="Textinput-Control" and @value="Новый документ"]')
        BUTTON_DISK = (By.XPATH, '//a[@href = "https://360.yandex.ru/?from=yandexid"]')
        BTN_SAVE = (By.CSS_SELECTOR,
        '.Button2.Button2_view_action.Button2_size_m.confirmation-dialog__button.confirmation-dialog__button_submit')
        BTN_ENTER_TO_YANDEX_ID = (By.CSS_SELECTOR,
                '.base-login-button__loginButtonText-cT.base-button__childrenContent-DJ')


    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.timeout = timeout

    def open(self):
        self.driver.get(self.Locators.BASE_URL)

    def go_to_disk(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BUTTON_DISK)).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_DISK)).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_GOTO_DISK)).click()

    def click_checkbox_im_not_robot(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.CHECKBOX)).click()

    def click_btn_enter_to_yandex(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_ENTER_TO_YANDEX)).click()
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_ENTER_TO_YANDEX_ID)).click()

    def create_folder(self, name_folder):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CREATE)).click()
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CREATE_FOLDER)).click()
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_NAME_FOLDER))
        element.clear()
        sleep(3)
        element.send_keys(name_folder)
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_SAVE)).click()

    def create_file(self, name_text_file):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CREATE)).click()
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CREATE_TEXT_FILE)).click()
        sleep(2)
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_NAME_TEXT_FILE))
        element.send_keys(name_text_file)
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_SAVE)).click()
        sleep(3)

    def close_created_file(self, name_text_file):
        # Локатор заголовка новой вкладки
        new_tab_title_locator = (By.XPATH, f'//title[contains(text(), "{name_text_file}.docx - Яндекс Документы")]')
        self.driver.switch_to.window(self.driver.window_handles[-1])   # Переключаемся на новую вкладку
        # Дожидаемся загрузки заголовка новой вкладки
        self.wait.until(EC.presence_of_element_located(new_tab_title_locator))
        # sleep(10)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])  # Переключаемся обратно на предыдущую вкладку

    def check_created_file(self, name_text_file):
        # locator_created_file = (By.XPATH, f'//div[@class="listing-item" and .//@aria-label="{name_text_file}.docx"]')
        locator_created_file = (By.XPATH, f'//div[contains(@class, "listing-item__title") '
                                          f'and @aria-label="{name_text_file}.docx"]')
        try:
            return self.wait.until(EC.visibility_of_element_located(locator_created_file))
        except TimeoutException:
            return None


    def find_and_open_folder(self, name_folder):
        locator_created_folder = (By.XPATH, f'//div[contains(@class, "listing-item_theme_tile") '
                                    f'and .//span[@class="clamped-text" and text()="{name_folder}"]]')
        actions = ActionChains(self.driver)
        created_folder_element = self.wait.until(EC.visibility_of_element_located(locator_created_folder))
        actions.double_click(created_folder_element).perform()
        sleep(2)


    def login_to_yandex(self, login, password):
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_FIELD)).send_keys(login)
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_ENTER_TO_YANDEX)).click()
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_FIELD_PASSWORD)).send_keys(password)
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_ENTER_TO_YANDEX)).click()

    def logout(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_USER_ACCOUNT)).click()
        sleep(2)
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_USER_ACCOUNT_LOGOUT)).click()

