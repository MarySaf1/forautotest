from xml.sax.xmlreader import Locator

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Base:
    def __init__(self):
        def find(self, locator: Locator, timeout: int = None):
            self.wait_for_ready_state_complete()
            try:
                return self.wait_present(locator, timeout)
            except TimeoutException:
                raise NoSuchElementException(f"Не удалось найти локатор '{locator}'")

        def __wait(self, method, message="", wait_method: str = "until", timeout: float = None):
            if not timeout:
                timeout = self.timeout
            web_driver_wait = WebDriverWait(self.browser.wd, timeout)
            wait_func = getattr(web_driver_wait, wait_method, None)
            if wait_func is None:
                raise AttributeError(f"Вебдрайвер не содержит метода '{wait_method}'")
            return wait_func(method, message)

        def wait_present(self, locator: Locator, timeout: int = None, message: str = None):
            if not message:
                message = f"Элемент '{locator}' не появился на странице"
            return self.__wait(
                method=ec.presence_of_element_located((locator.by, locator.value)),
                message=message,
                timeout=timeout
            )
