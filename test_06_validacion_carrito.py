import pytest
from selenium.webdriver.common.by import By
import time


def test_carrito_suma_total(driver):
    # 1. Login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 2. Agregar productos (Guardamos los precios para sumar después)
    # Seleccionamos: Mochila ($29.99) y Fleece Jacket ($49.99)
    item1_price = 29.99
    item2_price = 49.99

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

    # 3. Ir al carrito y avanzar al checkout
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    # 4. Completar datos de envío (Requisito para ver el total)
    driver.find_element(By.ID, "first-name").send_keys("Ezequiel")
    driver.find_element(By.ID, "last-name").send_keys("Parisi")
    driver.find_element(By.ID, "postal-code").send_keys("1824")
    driver.find_element(By.ID, "continue").click()

    # 5. VALIDACIÓN DE LÓGICA
    # Obtenemos el texto del subtotal (Ej: "Item total: $79.98")
    subtotal_texto = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text

    # Limpiamos el texto para quedarnos solo con el número
    # "Item total: $79.98" -> "79.98"
    subtotal_limpio = float(subtotal_texto.split("$")[1])

    # Verificamos que la suma de nuestros items coincida con lo que dice la página
    suma_esperada = item1_price + item2_price

    assert subtotal_limpio == suma_esperada, f"Error: La suma esperaba era {suma_esperada} pero el sistema muestra {subtotal_limpio}"

    print(f"\nValidación exitosa: {suma_esperada} == {subtotal_limpio}")