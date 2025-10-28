def test_inventario(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    # Verifica el título de la página
    titulo = driver.find_element("class name", "title").text
    assert titulo == "Products"

    # Verifica que haya productos
    productos = driver.find_elements("class name", "inventory_item")
    assert len(productos) > 0

    # Lista nombre y precio del primer producto
    nombre = productos[0].find_element("class name", "inventory_item_name").text 
    precio = productos[0].find_element("class name", "inventory_item_price").text
    print(f"Primer producto: {nombre} - Precio: {precio}")
