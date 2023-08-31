import tkinter as tk
import speech_recognition as sr

def Speech_to_Text():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            # txtSpeech.insert(tk.END, text + "\n")
            
        except sr.UnknownValueError:
            # txtSpeech.insert(tk.END, "Could not recognize\n")
            print("Could not recognize")
            
        except sr.RequestError as e:
            # txtSpeech.insert(tk.END, f"Error {e}\n")
            print(f"Error {e}")
            
flag = True
while flag:
    if int(input("Press 1 to speak: ")) == 1:
        Speech_to_Text()
    else:
        print("Bye")
        flag = False
    
    
