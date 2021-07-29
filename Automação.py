import os
import pyautogui
import time
import random

pyautogui.PAUSE = 0.5
videos_rodados = 0

# irá passar 300 vídeos
while videos_rodados < 300:
    videos_rodados += 1

    tempo = random.randint(5, 15)

    print(f'A quantidade de vídeos: {videos_rodados}')
    print(f'Tempo assistindo o vídeo: {tempo}')

    # Aleatorizando se vai curtir o vídeo
    time.sleep(tempo)
    curtidas = random.randint(1, 2)

    if curtidas == 2:
        print('Irá curtir: Sim')
        pyautogui.click(x=886, y=570)
    else:
        print('Irá curtir: Não')

    time.sleep(1)
    pyautogui.drag(0, -100)
    pyautogui.move(0, 100)

# Encerrando emulador
os.system('TASKKILL /F /IM Nox.exe')
time.sleep(10)

# Desligando o computador
os.system("shutdown /s /t 1")