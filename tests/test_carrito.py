from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_carrito(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    wait = WebDriverWait(driver, 10)

    # Agregar primer producto al carrito
    boton_add = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(),'Add to cart')])[1]")))
    boton_add.click()

    # Verificar contador del carrito
    contador = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))).text
    assert contador == "1"

    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Validar que el encabezado "Your Cart" esté visible
    cart_header = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Your Cart']")))
    assert "Your Cart" in cart_header.text
