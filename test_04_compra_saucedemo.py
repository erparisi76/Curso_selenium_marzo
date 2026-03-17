# test_compra_saucedemo.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_and_purchase(driver): # Pytest toma el 'driver' del conftest.py
    wait = WebDriverWait(driver, 10)

    # Navegación
    driver.get("https://www.saucedemo.com/")

    # Login
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Agregar al carrito e ir al Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # Formulario de envío
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Ezequiel")
    driver.find_element(By.ID, "last-name").send_keys("Parisi")
    driver.find_element(By.ID, "postal-code").send_keys("1824")
    driver.find_element(By.ID, "continue").click()

    # Finalizar
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    # Verificación final
    assert "checkout-complete.html" in driver.current_url
    time.sleep(2)