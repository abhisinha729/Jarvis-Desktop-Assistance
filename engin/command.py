# voice of jarvis
import pyttsx3
import speech_recognition as sr
import eel
import time
def speak(text):
  engine=pyttsx3.init("sapi5")
  voices = engine.getProperty('voices') 
  engine.setProperty('voice', voices[1].id) 
  engine.setProperty('rate', 170)
  eel.DisplayMessage(text)
#   print(voices)
  engine.say(text)
  engine.runAndWait()
  

def take_command():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        eel.DisplayMessage("listening..")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)

        audio=r.listen(source,10,6)
    try:
        print("recognizing")
        eel.DisplayMessage("recognizing")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said:{query}")
        eel.DisplayMessage(query)
        time.sleep(1)
        # speak(query)
        
    except Exception as e:
        return " "    
    return query.lower()

@eel.expose
def all_Commands():
    try:
        query=take_command()
        print(query)
    
        if "open" in query:
           from engin.features import open_Command
           open_Command(query)
        elif "on youtube" in query:
           from engin.features import PlayYoutube
           PlayYoutube(query)  
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engin.features import find_contacts,whatsApp
            message=""
            contact_no,name=find_contacts(query)  
            if (contact_no !=0):
                
                if  "send message" in query:
                    flag="message"
                    speak("what message to send")
                    query=take_command()

                elif "phone call" in query:
                    flag="call"
                else:
                    flag="video call"
                whatsApp(contact_no,query,flag,name)

        else:
          print("not run")    
    except Exception as e:
        print("error",e)
    eel.ShowHood()
    

