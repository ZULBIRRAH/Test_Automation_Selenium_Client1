from pages.login_page import LoginPage

def test_valid_login(driver):
    login = LoginPage(driver)
    login.enter_username("validUser")
    login.enter_password("validPassword123")
    login.click_login()
    assert "dashboard" in driver.current_url.lower()

def test_invalid_login(driver):
    login = LoginPage(driver)
    login.enter_username("invalidUser")
    login.enter_password("wrongPassword")
    login.click_login()
    assert login.get_error_message() == "Invalid username or password."
