import time
import pyautogui as pyautogui

print('Iniciando programa')

# print(pyautogui.position())
pyautogui.press('win')
pyautogui.write('opera')
time.sleep(2)
pyautogui.press('enter')
time.sleep(7)
pyautogui.press('n')
time.sleep(4)
pyautogui.write('tweet feito pelo bot escravo do leo.')
time.sleep(1)
pyautogui.click(x=1232, y=465)

print('Tweet feito!')

''' Classe usada pra descobrir o pixel do click
import time
import pyautogui as pyautogui

for i in range(1, 6):
    print(f'{i}')
    time.sleep(1)

print(pyautogui.position())'''