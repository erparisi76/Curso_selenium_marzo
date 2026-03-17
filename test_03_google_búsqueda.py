import random
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# --- 1. EL FIXTURE (Configuración avanzada de sigilo) ---
@pytest.fixture
def driver():
    options = Options()
    # Deshabilitar barra de automatización
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # User-Agent realista
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

    # Deshabilitar detección de automatización
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)

    # Script para eliminar el flag navigator.webdriver
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    })

    driver.maximize_window()

    yield driver  # Entrega el driver al test

    driver.quit()  # Cierra al terminar


# --- 2. EL TEST ---
def test_google_search_urquiza(driver):
    wait = WebDriverWait(driver, 10)

    # Navegar a Google
    driver.get("https://www.google.com")

    # Pausa aleatoria humana
    time.sleep(random.uniform(1.0, 2.0))

    # Localizar buscador por ID
    buscador = wait.until(EC.visibility_of_element_located((By.ID, "APjFqb")))

    # Escribir y presionar ENTER
    texto_busqueda = "Justo José de Urquiza"
    buscador.send_keys(texto_busqueda)
    time.sleep(random.uniform(0.5, 1.0))
    buscador.send_keys(Keys.ENTER)

    # Esperar y verificar el primer resultado (CSS Selector h3)
    primer_resultado = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3")))

    # --- 3. ASERCIÓN (Validación) ---
    # Verificamos que el texto del primer título contenga algo relacionado a la búsqueda
    print(f"\nResultado encontrado: {primer_resultado.text}")
    assert "Urquiza" in primer_resultado.text

    # Pausa final opcional para inspección visual
    time.sleep(3)