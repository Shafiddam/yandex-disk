import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def get_disk_resources():
    def _get_disk_resources(url, headers):
        response = requests.get(url, headers=headers)
        return response
    return _get_disk_resources


@pytest.fixture
def get_disk():
    def _get_disk(url, headers):
        response = requests.get(url, headers=headers)
        return response
    return _get_disk

@pytest.fixture
def get_disk_resources_files():
    def _get_disk_resources_files(url, headers):
        response = requests.get(url, headers=headers)
        return response
    return _get_disk_resources_files


@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--lang=en-US")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1280,800")
    chrome_options.add_argument("--allow-insecure-localhost")
    driver_path = "c:\\Chromedriver\\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    return driver
