# 🧪 QA Automation Framework - Selenium & Python

Este repositorio contiene un framework de automatización de pruebas **End-to-End (E2E)** diseñado para validar flujos de usuario en aplicaciones web como [SauceDemo](https://www.saucedemo.com/) y motores de búsqueda. Está construido con estándares profesionales de la industria, integrando ejecución en la nube y reportes visuales detallados.

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.10+
* **Framework de Pruebas:** Pytest
* **Automatización Web:** Selenium WebDriver (Chrome)
* **Reportes:** Allure Framework & Pytest-HTML
* **CI/CD:** GitHub Actions
* **Hosting de Reportes:** GitHub Pages

## 📋 Características Principales

* **Ejecución en la Nube:** Configurado con un pipeline `.yml` para correr en servidores Ubuntu de forma invisible (Headless mode).
* **Evidencia Automática:** Captura de pantalla automática (vía `conftest.py`) adjunta al reporte cada vez que un test falla.
* **Reportes Duales:** Generación simultánea de un reporte HTML estático y un panel interactivo de Allure.

## 🧪 Casos de Prueba Automatizados (Test Suite)

Actualmente, la suite incluye la validación de los siguientes escenarios:
1. **Flujo de Compra Exitoso (`test_04_compra_saucedemo`):** Validación End-to-End desde el login, agregado al carrito y checkout final.
2. **Validación de Errores (`test_05_compra_saucedemo_error`):** Comprobación del manejo de errores durante el proceso de compra.
3. **Búsquedas Dinámicas (`test_03_google_busqueda`):** Interacción con barras de búsqueda y validación de resultados.
4. **Localizadores Complejos (`test_01_xpath` & `test_02_xpath_simple`):** Pruebas de robustez utilizando selectores XPath avanzados.

## 🚀 Instalación y Uso Local

Para correr este proyecto en tu propia máquina, sigue estos pasos:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/erparisi76/Curso_selenium_marzo.git](https://github.com/erparisi76/Curso_selenium_marzo.git)
cd Curso_selenium_marzo
2. Instalar las dependencias
Asegúrate de tener Python instalado y ejecuta:

Bash
pip install -r requirements.txt

3. Ejecutar las pruebas
Para correr todos los tests y generar los reportes al mismo tiempo:

Bash
pytest --html=reporte.html --self-contained-html --alluredir=allure-results

4. Visualizar el reporte interactivo (Allure)
Bash
allure serve allure-results
📈 Integración Continua y Reportes Online
Este proyecto utiliza GitHub Actions para ejecutar la suite de pruebas automáticamente en cada subida de código (push) a la rama principal o de forma manual (workflow_dispatch).

Los resultados históricos y gráficos de tendencia se publican y actualizan automáticamente. Puedes ver el último reporte generado en el siguiente enlace:

🔗 Ver Reporte de Allure en Vivo

Desarrollado por Ezequiel R. Parisi | QA Automation Engineer
