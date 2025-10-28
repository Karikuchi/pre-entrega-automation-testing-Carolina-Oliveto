def test_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    # Validación de login exitoso
    assert "inventory.html" in driver.current_url
    assert "Swag Labs" in driver.page_source
