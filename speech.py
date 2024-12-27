import speech_recognition

 
r = speech_recognition.Recognizer()
def voice_out():
    
    with speech_recognition.Microphone() as source:
           r.adjust_for_ambient_noise(source)
           print('listening...')
           audio = r.listen(source)
           text = 'testing-text'
           try :
                text = r.recognize_google(audio,language ='en-in')
                return text
           except Exception as e:
                  print(e)

