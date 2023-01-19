import pyautogui
import time

var = pyautogui.alert
pyautogui.PAUSE = 0.5

# Abrir o Google Drive no computador
pyautogui.press('winleft')
pyautogui.write('microsoft edge')
pyautogui.press('enter')
# time.sleep(1)
pyautogui.write('https://drive.google.com/drive')
pyautogui.press('enter')

# Entrar na área de trabalho

pyautogui.hotkey('winleft', 'd')

# Clicar no arquivo e arrastar

pyautogui.moveTo(567, 38)
pyautogui.moveDown()
pyautogui.moveTo(756, 635)

# Enquanto estiver arrastando mudar para a página do Google Drive

pyautogui.hotkey('alt', 'tab')

# Soltar o arquivo dentro do Google Drive

pyautogui.mouseUp()

# Esperar alguns segundos

time.sleep(5)

pyautogui.alert("O código foi finalizado. Você ja pode utilizar o computador!")
