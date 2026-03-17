import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_and_purchase(driver):
    wait = WebDriverWait(driver, 10)

    # 1. Navegación y Login
    driver.get("https://www.saucedemo.com/")
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 2. Agregar al carrito
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

    # 3. Ir al carrito (Aquí es donde se ve tu imagen)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # --- NUEVA VERIFICACIÓN (Basada en tu foto) ---
    producto_titulo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))).text
    assert producto_titulo == "Sauce Pytest Backpack"
    print(f"Validación exitosa: El producto en el carrito es {producto_titulo}")

    # 4. Continuar con el Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # 5. Formulario de envío
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Ezequiel")
    driver.find_element(By.ID, "last-name").send_keys("Parisi")
    driver.find_element(By.ID, "postal-code").send_keys("1824")
    driver.find_element(By.ID, "continue").click()

    # 6. Finalizar
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    # Verificación final de URL
    assert "checkout-complete.html" in driver.current_url
    time.sleep(2)