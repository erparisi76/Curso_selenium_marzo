import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# --- 1. FIXTURE PARA EL NAVEGADOR ---
@pytest.fixture
def driver():
    # Configuramos opciones para evitar popups y barra de automatización
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # Inicialización del driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    yield driver  # Aquí se ejecuta la prueba

    # Cierre automático (Teardown)
    driver.quit()


# --- 2. EL TEST ---
def test_submit_textbox_form(driver):
    wait = WebDriverWait(driver, 10)

    # Navegación
    driver.get("https://demoqa.com/text-box")

    # Nombre Completo
    # Usamos ID ya que es más estable y rápido que XPATH
    nom = wait.until(EC.visibility_of_element_located((By.ID, "userName")))
    nom.send_keys("Ezequiel")

    # Email
    driver.find_element(By.ID, "userEmail").send_keys("ezequiel@gmail.com")

    # Dirección Actual
    driver.find_element(By.ID, "currentAddress").send_keys("Dirección actual")

    # Dirección Permanente
    driver.find_element(By.ID, "permanentAddress").send_keys("Dirección permanente")

    # Botón Submit
    btn_submit = driver.find_element(By.ID, "submit")

    # Hacemos scroll hasta el botón
    driver.execute_script("arguments[0].scrollIntoView();", btn_submit)

    # TIP: En DemoQA a veces el click estándar falla por anuncios.
    # Usar JavaScript para el click es una técnica de salvación común:
    driver.execute_script("arguments[0].click();", btn_submit)

    # --- 3. ASERCIÓN (Validación del resultado) ---
    # Verificamos que aparezca el cuadro de resultados (id='output')
    output_box = wait.until(EC.visibility_of_element_located((By.ID, "output")))

    # Validamos que el nombre mostrado en el resultado sea el correcto
    resultado_nombre = driver.find_element(By.ID, "name").text
    assert "Ezequiel" in resultado_nombre

    print("Prueba de Text Box exitosa")
    time.sleep(2)