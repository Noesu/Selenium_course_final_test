import pytest
from pages.product_page import ProductPage

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
