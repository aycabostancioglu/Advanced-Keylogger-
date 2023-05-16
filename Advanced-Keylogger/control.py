from pynput.mouse import Controller
from pynput.keyboard import Controller
def controlMouse():
    mouse = Controller()
    mouse.position = (300,200) #ekranın solunu 0,0 gibi düşün soldan sağa doğru hareket


def controlKeyboard():
    keyboard =Controller()
    keyboard.type("SELAM!")

controlKeyboard()
