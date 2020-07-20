from pynput.mouse import Listener

import logging

logging.basicConfig(filename="mouse_config.txt", level=logging.INFO, format='%(message)s')
file = open('mouse_config.txt', 'rb')
if file.readline():
    for line in file:
        pass
    counter = int(line.decode())
else:
    counter = 0
file.close()

def on_click(x, y, button, pressed):
    global counter
    if pressed:
        counter += 1
        logging.info(str(counter))

with Listener(on_click=on_click) as listener:
    listener.join()