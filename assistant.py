from autogen import UserProxyAgent
from autogen.agentchat.contrib.teachable_agent import TeachableAgent,TextAnalyzerAgent
from dotenv import load_dotenv
import os
from autogen.code_utils import extract_code
import main
import speech
import json
import csv


load_dotenv()
try:
    from termcolor import colored
except ImportError:
    def coloured(x,*args,**kwargs,):
        return x


config = [{
    "model" : 'gpt-3.5-turbo',
    "api_key" :os.getenv('api_key'),
},{"model" : 'gpt-3.5-turbo-0613',"api_key":os.getenv('api_key')
}
]


llm_config = {'config_list':config,'cache_seed':42,'context' : 'you are a AI assistant teacher for eye impaired childrens'}

teach_config = {
    "recall_threshold": 1.5,
    "verbosity":3,
    "path_to_db_dir" : "C:\\Users\\ASUS\\Desktop\\SNUPROJECTX\\db",
    'reset_db':False
    }




    

jisu = TeachableAgent(name='jisu',
                         system_message='you are a AI assistant teacher for eye impaired childrens,You are a caring teacher and you love to teach others',
                         llm_config=llm_config,
                         teach_config=teach_config)

user = UserProxyAgent(name='user',human_input_mode='ALWAYS',code_execution_config = True ,max_consecutive_auto_reply=0)

analyzer  =  TextAnalyzerAgent(name = 'analyzer',llm_config=llm_config)


@user.register_for_execution(name="reverse")
@jisu.register_for_llm(name="reverse",description='to reverse the given text')
def reverse(text: str) -> str:
    return text[::-1]
path = 'assesment.csv'
def teachermode():
    print('username : admin[default]')
    password =  input('Password :')
    if password == 'admin':
        print('1.to give assignment \n 2. change model')
        opt = input()
        if opt == 'give assingnment' or '1':
           global path
           path = input('you can create a csv file and give the path :')
        if opt == 'exit':
            main.main()
        if opt == '2':
            x = input('enter the model name')
            config[0]['model'] = x
            

                
        

text='how may i assist you? today'
def assistancemode():
       user.receive(text,jisu)
        
       while True:
           print(f'{colored("user",color="cyan")} (to teacher):')
           try:
                prompt = speech.voice_out()
                prompt = input()
                human_input = [{'role': 'user','content':prompt}]
                analyzed = analyzer.analyze_text(prompt,'Is there any thing about the assesment or schedule REPLY ONLY YES OR NO ')
           except TypeError:
                 print('trying again')
                 prompt = speech.voice_out()
                 #prompt = input()
                 human_input = [{'role': 'user','content':prompt}]
                      
           if analyzed == 'YES':
               main.engine.say('the shedule for today is :')
               
               main.engine.runAndWait()
               from datetime import date
               today = date.today()
               stoday = date.isoformat(today)
               
               
               with open(path,'r',newline='') as f:
                 reader = csv.reader(f)
                 next(reader)
                 for row in reader:
                     if row[0] == stoday:
                         task = row[1]
                         main.engine.say(task)
                         main.engine.runAndWait()
                         print(f'{colored("jisu",color="magenta")} (to user):')
                         print(task)
                         break 
           else:                       
               reply = jisu._generate_teachable_assistant_reply(messages=human_input)
               print(reply)
               checker = isinstance(reply[1],dict)
               print(checker)
               main.engine.say(reply[1])
               main.engine.runAndWait()
               
               if prompt == 'exit':
                   main.main()
               elif checker == True:
                   func_name =reply[1]['function_call']['name']
                   arguments_str = reply[1]['function_call']['arguments']
                   
                   # Convert arguments from a string to a dictionary
                   arguments = json.loads(arguments_str)
                   print(arguments,' debugging print')
                   # Check if the function exists
                   if func_name in globals() and callable(globals()[func_name]):
                       # Call the function with the provided arguments
                       result = globals()[func_name](**arguments)
                       print(f'{colored("jisu",color="magenta")} (to user):')
                       print(result)
                              
              
               else:
                       print(f'{colored("jisu",color="magenta")} (to user):')
                       user.receive(reply[1],jisu)      
            
               
               
def feedbackmode():
       user.receive(text,jisu)
       while True:
          print(f'{colored("user",color="cyan")} (to teacher):')
          
          try:
               prompt = speech.voice_out()
               #prompt = input()
               human_input = [{'role': 'user','content':prompt}]
               analyzed = analyzer.analyze_text(prompt,'Is there any thing about the assesment or schedule REPLY ONLY YES OR NO ')
          except TypeError:
                print('trying again')
                prompt = speech.voice_out()
                #prompt = input()
                human_input = [{'role': 'user','content':prompt}]
                analyzed = analyzer.analyze_text(prompt,'Is there any thing about the assesment or schedule REPLY ONLY YES OR NO ')
          
          if analyzed == 'YES':
              main.engine.say('the shedule for today is :')
              
              main.engine.runAndWait()
              from datetime import date
              today = date.today()
              stoday = date.isoformat(today)
              
              
              with open(path,'r',newline='') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    if row[0] == stoday:
                        task = row[1]
                        main.engine.say(task)
                        main.engine.runAndWait()
                        print(f'{colored("jisu",color="magenta")} (to user):')
                        print(task)
                        break 
          else:                       
              reply = jisu._generate_teachable_assistant_reply(messages=human_input)
              #print(reply)
              checker = isinstance(reply[1],dict)
              #print(checker)
              main.engine.say(reply[1])
              main.engine.runAndWait()
              
              if prompt == 'exit':
                  main.main()
              elif checker == True:
                  func_name =reply[1]['function_call']['name']
                  arguments_str = reply[1]['function_call']['arguments']
                  
                  # Convert arguments from a string to a dictionary
                  arguments = json.loads(arguments_str)
                  print(arguments,' debugging print')
                  # Check if the function exists
                  if func_name in globals() and callable(globals()[func_name]):
                      # Call the function with the provided arguments
                      result = globals()[func_name](**arguments)
                      print(f'{colored("jisu",color="magenta")} (to user):')
                      print(result)
                             
              elif prompt == 'learn':
                      jisu.learn_from_user_feedback()
                      jisu.close_db()
              else:
                      print(f'{colored("jisu",color="magenta")} (to user):')
                      user.receive(reply[1],jisu)
                            
                   
              
              
def feedbackmodule():
    user.initiate_chat(jisu,clear_history=True,message = 'how can i assist you?')  
    jisu.learn_from_user_feedback()  
if __name__ == '__main__':
    feedbackmode()
   