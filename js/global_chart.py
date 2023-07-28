import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image, ImageOps
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializace prohlížeče
options = Options()
options.add_argument("--headless")  # Spuštění prohlížeče v headless módu (bez viditelného okna)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Načtení stránky s iframe
driver.get("https://app.koyfin.com/share/6faf725b56/simple")

# Počkejte, až se stránka načte (změňte dobu podle potřeby)
time.sleep(5)  # Počká 5 sekund (můžete upravit)

# Počkejte, až se iframe načte
wait = WebDriverWait(driver, 30)  # Změňte na delší dobu, pokud je potřeba
iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
driver.switch_to.frame(iframe)

# Zachytění screenshotu stránky s iframe
screenshot = driver.get_screenshot_as_png()

# Uložení screenshotu jako obrázek
with open("global_chart.png", "wb") as file:
    file.write(screenshot)

# Otevření obrázku s pomocí Pillow
image = Image.open("global_chart.png")

# Přidání bílého okraje
border_size = 5
image_with_border = ImageOps.expand(image, border=border_size, fill="white")

# Uložení obrázku s bílým okrajem
image_with_border.save("global_chart_with_border.png")

# Ukončení prohlížeče
driver.quit()
