from pages.home_page import HomePage
def test_correct_login(driver):
    homepage = HomePage(driver)
    homepage.open_website()
    homepage.login("standard_user","secret_sauce")
    assert homepage.is_on_page() == "Products"
    homepage.add_to_cart()
    homepage.go_to_your_cart_page()
    assert homepage.is_on_page() == "Your Cart"
    assert homepage.is_first_item_here() == "Sauce Labs Bike Light"
    assert homepage.is_second_item_here() == "Sauce Labs Backpack"
    homepage.go_to_checkout() 
    assert homepage.is_on_page() == "Checkout: Your Information"
    homepage.checkout_informations("Amira", "Hadžipašić", "71000")
    homepage.go_to_continue()
    assert homepage.is_on_page() == "Checkout: Overview"
    assert homepage.is_first_item_here() == "Sauce Labs Bike Light"
    assert homepage.is_second_item_here() == "Sauce Labs Backpack"
    homepage.go_to_finish()
    assert homepage.is_on_page() == "Checkout: Complete!"
    homepage.go_to_logout()
    assert homepage.is_on_login_page() == "login_credentials"
