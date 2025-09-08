import os
import re
from shlex import quote
import struct
import subprocess
import time
from playsound import playsound
import eel
import pyaudio
import pyautogui
from engin.command import speak
from engin.config import ASSISTANT_NAME
import pywhatkit as kit
import webbrowser
import sqlite3

from engin.helper import extract_yt_term, remove_words

import pvporcupine


conn=sqlite3.connect("jarvis.db")
cursor=conn.cursor()

# playing assistant sound function
@eel.expose
def playAssistantSound():
    music_direct="www\\assets\\audio\\start_audio.mp3"
    playsound(music_direct)

# open_Command is function that take query
def open_Command(query):
    # Clean query
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower()
    
    app_name=query.strip()

    if app_name!="":
        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name = ?',(app_name,))
            results=cursor.fetchall()

            if len(results)!=0:
                speak("Opening" +query)
                os.startfile(results[0][0])
            elif len(results)==0:
                cursor.execute('SELECT url FROM web_command WHERE name = ?',(app_name,))
                results=cursor.fetchall() 

                if len(results)!=0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])
                else:
                    speak("Opening "+query)
                    try:
                        os.system("start "+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")

             
             
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    print("playing " + search_term + " on YouTube")
    kit.playonyt(search_term)

def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
        
        #pre trained keywords
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"])
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)

        #loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            #processing keywords comes from mic
            keyword_index=porcupine.process(keyword)

            #checking first keyword detected for not
            if keyword_index>=0:
                print("hotword detected")
                
                #pressing shortcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
    except Exception as e:
        print("Error:",e)
    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()


#find contacts in database 
def find_contacts(query):
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call',
                       'send', 'message', 'whatsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query=query.strip().lower()
        cursor.execute(
            "SELECT name, mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?",
            ('%' + query + '%', query + '%')
        )
        result = cursor.fetchall()
        print(result[0][0])
        mobile_number_str=str(result[0][0])

        

        # ensure mobile starts with +91
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str,query

    except Exception as e:
        print("DB error:", e)
        speak("not exist in contacts")
        return 0,0




def whatsApp(mobile_no, message, flag, name):
    if flag == 'message':
        target_tab = 12
        jarvis_message = "Message sent successfully to " + name
    
    elif flag == 'call':
        target_tab = 7
        message = ""  # no text needed for calls
        jarvis_message = "Calling " + name
    
    else:  # video call
        target_tab = 6
        message = ""
        jarvis_message = "Starting video call with " + name

    # encode the message for url
    encoded_message = quote(message)

    # construct WhatsApp URL
    whatsApp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    #construct the full command
    full_command=f'start "" "{whatsApp_url}"'
    
    #open whatsapp with the construct url using cmd.exe
    subprocess.run(full_command,shell=True)
    time.sleep(5)
    subprocess.run(full_command,shell=True)


    pyautogui.hotkey('ctrl','f')


    # press tab and enter (to simulate send)
    for i in range(1,target_tab):
        pyautogui.hotkey('tab')
    pyautogui.hotkey("enter")

    speak(jarvis_message)


    
            
                



            





    
