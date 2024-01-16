from pynput import *
import pyautogui as ai
import threading
import time



keys = []
ctrl_pressed = False
button_pressed = False

  
def on_press(key):
     
    keys.append(key)
    global ctrl_pressed
     
    try:
        if key == keyboard.Key.esc:
            print('Escape pressed. Exiting...')
            return False
        
        if key == keyboard.Key.ctrl:
            ctrl_pressed = True
            
            
        
         
    except AttributeError:
        
        if key == keyboard.Key.esc:
            print('Escape pressed. Exiting...')
            return False
        
def on_key_release(key):
    global ctrl_pressed
    try:
        if key == keyboard.Key.ctrl:
            ctrl_pressed = False
            
    except AttributeError:
        pass
        
        
            
        
def on_click(x, y, button, pressed):
    global button_pressed
    if button == mouse.Button.left:
      button_pressed = pressed




# Collect events until released

def start_mouse_listener():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

def start_keyboard_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_key_release) as listener:
        listener.join()
        
keyboard_thread = threading.Thread(target=start_keyboard_listener)
mouse_thread = threading.Thread(target=start_mouse_listener)


keyboard_thread.start()
mouse_thread.start()

while True:
    time.sleep(0)
    if button_pressed and ctrl_pressed:
        for i in range(5):
            
            ai.click(clicks=3)