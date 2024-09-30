import pyautogui as pato
import time
from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')
# print(date)

# Navega pela Área de Trabalho até o Chrome
pato.press('winleft')
time.sleep(1)
pato.write('chrome', 0.2)
time.sleep(1)
pato.press('enter')
time.sleep(1)

# Realiza a Pesquisa
pato.moveTo(319, 85, 1.5)
pato.click()
pato.write('ibovespa hoje', 0.2)
time.sleep(1)
pato.press('enter')
time.sleep(1)

# Tira a printscreen e volta para o Vs Code
pato.screenshot(f'pscreen_email/ibovespa_{date}.png')
time.sleep(1)
pato.hotkey('alt', 'tab')
time.sleep(1)

# Executa o Script de enviar o Email
pato.moveTo(1016, 749, 1)
time.sleep(1)
pato.write('python ps', 0.2)
time.sleep(1)
pato.press('tab')
time.sleep(1)
pato.write('email', 0.2)
time.sleep(1)
pato.press('tab')
time.sleep(1)
pato.press('enter')



