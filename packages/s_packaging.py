# --coding:utf-8--


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import By
from selenium.webdriver.common.keys import Keys
from common.parseconfig import parseConfig


class packaging():
    def __init__(self, sections, ini_dir):
        self.sections = sections
        self.ini_dir = ini_dir
        self.parse = parseConfig(self.sections, self.ini_dir)

    def wait_element_appear(self, driver, ini_key, timeout=10):
        by, value = self.parse.split_content(ini_key)
        paraser_by(by)
        WebDriverWait(driver, timeout, 1, ).until(lambda x: x.find_element(eval(by), value).is_displayed())

    def write_obj(self, driver, ini_key, *args):
        by, value = self.parse.split_content(ini_key)
        paraser_by(by)
        driver.find_element(eval(by), value).send_keys(*args)

    def click_obj(self, driver, ini_key):
        by, value = self.parse.split_content(ini_key)
        paraser_by(by)
        driver.find_element(eval(by), value).click()

    def waiting_obj(self, driver, ini_key):
        by, value = self.parse.split_content(ini_key)
        paraser_by(by)
        self.wait_element_appear(self, driver, timeout=10, by=eval(by), value=value)


def paraser_by(by):
    if by == 'By.XPATH':
        by = By.XPATH
    elif by == 'By.ID':
        by = By.ID
    elif by == 'By.NAME':
        by = By.NAME
    return by


if __name__ == '__main__':
    click_obj('dfd', [1, 2])