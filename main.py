import speech
import assistant
import pyttsx3

label  = """\n
\t\t\t\t░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
\t\t\t\t░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
\t\t\t\t░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
\t\t\t\t░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
\t\t\t\t░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
\t\t\t\t░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
"""



try:
    from termcolor import colored
except ImportError:
    def coloured(x,*args,**kwargs,):
        return x

engine = pyttsx3.init()
def main():
    print(f'\n\n\tMAKE YOUR CHOICE\n1.For assistance mode \n 2.For feedback \n3.for teacher mode')
    engine.say('SAY your choice , 1 , For assistance mode ,2 , For feedback 3 for teacher mode')
    engine.runAndWait()
    x=speech.voice_out()
    print(f'debug print ignore : {x}')#for debugging purpose
    if x == 'assistance mode' or x == 'assistant mode':
        engine.say('you have chossen for assistance mode')
        engine.runAndWait()
        assistant.assistancemode()       
        
    elif x == 'feedback mode':
        engine.say('you have choose to learn from feedback mode')
        engine.runAndWait()
        assistant.feedbackmode()
        
    elif x == 'teacher mode':
       engine.say('your in teacher mode aka admin mode \n it\'s dangerous to operate without programming language')
       engine.runAndWait()
       
    else:
        engine.say('you have chossen for assistance mode')
        engine.runAndWait()
        assistant.assistancemode()       
       
    
       
       

if __name__ =='__main__':
 
    
    print(label)
    print('hello i\'m a AI assitant who helps the eye impaired childrens to learn better using by techonology.\nI can also learn from your feedback\n \t \t  ')
    main()
    
