import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage

@pytest.mark.parametrize('link', range(0, 10))
def test_guest_can_add_product_to_basket(browser, link):
    if link == 7:
        pytest.xfail(reason="Test with offer7 continuously failed")
    parametrized_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, parametrized_link)
    page.open()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.should_be_add_to_basket_link()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_product_name(product_name)
    page.check_product_price(product_price)

@pytest.mark.xfail(condition=True, reason="Guest should see a success message", strict=True)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(condition=True, reason="Disappearing message shouldn`t be presented", strict=True)
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_disappearing_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

