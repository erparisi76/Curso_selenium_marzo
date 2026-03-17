import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# --- 1. EL FIXTURE (Configuración y Ciclo de Vida) ---
@pytest.fixture
def driver():
    # Configuramos opciones para que el navegador abra limpio
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # Inicialización
    # Si necesitas la ruta manual, usa: service=Service("C:/Drivers/chromedriver.exe")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    yield driver  # Aquí se ejecuta el test

    # Teardown: Cierre automático al finalizar
    driver.quit()


# --- 2. EL TEST (La lógica de automatización) ---
def test_text_box_submission(driver):
    wait = WebDriverWait(driver, 10)

    # Navegación
    driver.get("https://demoqa.com/text-box")

    # Llenado de Formulario
    # Usamos wait.until para el primer elemento para asegurar que cargó la página
    nom = wait.until(EC.visibility_of_element_located((By.ID, "userName")))
    nom.send_keys("Ezequiel")

    driver.find_element(By.ID, "userEmails").send_keys("ezequiel@gmail.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Dirección actual")
    driver.find_element(By.ID, "permanentAddress").send_keys("Dirección permanente")

    # Botón Submit con Scroll
    btn_submit = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView();", btn_submit)

    # A veces en DemoQA hay banners que tapan el botón, el click por JS es más seguro:
    driver.execute_script("arguments[0].click();", btn_submit)

    # --- 3. VERIFICACIÓN (Assertion) ---
    # Verificamos que el cuadro de resultado aparezca después del click
    output = wait.until(EC.visibility_of_element_located((By.ID, "output")))

    # Validamos que el nombre en el resultado coincida
    res_name = driver.find_element(By.ID, "name").text
    assert "Ezequiel" in res_name

    print("Formulario enviado y verificado correctamente.")
    time.sleep(2)  # Solo para ver el resultado visualmente un momento