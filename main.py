import os
import eel
from engin.features import *
from engin.command import *
# from engin.features import hotword


def start():
    eel.init("www")
    playAssistantSound()

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html',mode=None,host='localhost',block=True)