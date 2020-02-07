from .pages.main_page import MainPage
#from selenium.common.exceptions import NoSuchElementException
from .pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_should_see_login_link(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}/"
    page = MainPage(browser, link)   
    page.open()                     #opening the page 
    page.go_to_login_page()         #goes to login page
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()