from selenium import webdriver
from config.config import settings
from urllib.parse import urljoin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

        self.wait = WebDriverWait(self.driver, 5)

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(settings['url'])

    def goto_page(self, page):
        self.driver.get(urljoin(settings['url'], page.lower()))

    def wait_for_correct_current_url(self, desired_url):
        desired_url = urljoin(settings['url'], desired_url.lower())
        self.wait.until(
            lambda driver: self.driver.current_url == desired_url)

    def wait_for_element_to_appear(self, xpath):
        element = self.wait.until(
            EC.presence_of_element_located((
                By.XPATH, xpath)))

    def close_browser(self):
        self.driver.quit()


webapp = WebApp.get_instance()
