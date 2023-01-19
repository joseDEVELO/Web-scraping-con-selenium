from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Options

from selenium.webdriver.chrome.options import Options

def iniciar_chrome():
    ruta = ChromeDriverManager(path="./chromedriver", log_level=0).install()

    options = Options()
    user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"

    options.add_argument(user_agent)
    options.add_argument("--start-maximized")
    options.add_argument("--disable-web-security")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--no-sandbox")
    options.add_argument("--allow-runing-insecure-content")
    options.add_argument("--no-first-run")
    options.add_argument("--no-proxy-server")
    options.add_argument("--disable-blink-features=AutomationControlled") 

    s = Service(ruta)
    driver = webdriver.Chrome(service=s, options=options)
    
    return driver


if __name__ == '__main__':
    driver = iniciar_chrome()
    input("Pulsa ENTER para salir")
    driver.quit()