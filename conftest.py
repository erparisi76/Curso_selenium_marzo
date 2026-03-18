import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# --- 1. CONFIGURACIÓN DEL DRIVER ---
@pytest.fixture(scope="function")
def driver(request):
    """
    Configura el navegador con opciones para evitar detección
    y permitir ejecución en la nube (CI/CD).
    """
    chrome_options = Options()

    # --- MODO HEADLESS (Para GitHub Actions) ---
    # Si quieres ver el navegador en tu PC, puedes comentar la siguiente línea.
    # Pero para GitHub Actions, ES OBLIGATORIA.

    chrome_options.add_argument("--headless=new")

    # Opciones de compatibilidad y privacidad
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # Evitar popups de contraseñas
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Inicialización del Driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # VINCULACIÓN: Permite que el capturador de pantalla acceda a esta instancia
    if request.node is not None:
        request.node.driver = driver

    yield driver

    # Cierre seguro
    driver.quit()


# --- 2. GENERADOR DE REPORTES (HTML + ALLURE) ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de Pytest que se activa al fallar un test.
    Genera capturas para Allure y para el reporte HTML clásico.
    """
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    # Verificamos si el fallo ocurrió durante la ejecución del test ('call')
    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)

        if driver:
            try:
                # A. Captura para ALLURE (Formato binario PNG)
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="Captura_Falla_Allure",
                    attachment_type=allure.attachment_type.PNG
                )

                # B. Captura para PYTEST-HTML (Formato Base64)
                import pytest_html
                screenshot_base = driver.get_screenshot_as_base64()
                extras.append(pytest_html.extras.image(screenshot_base, "Captura de la Falla"))

            except Exception as e:
                print(f"\n[!] Error al capturar pantalla: {e}")

    # Guardamos los extras en el reporte
    report.extras = extras