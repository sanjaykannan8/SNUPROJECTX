from autogen.agentchat.contrib.text_analyzer_agent import TextAnalyzerAgent
from dotenv import load_dotenv
import os
load_dotenv()
config = [{
    "model" : 'gpt-3.5-turbo',
    "api_key" :os.getenv('api_key'),
},{"model" : 'gpt-3.5-turbo-0613',"api_key":os.getenv('api_key')
}
]


llm_config = {'config_list':config,'cache_seed':42}

analyzer  =  TextAnalyzerAgent(name = 'analyzer',llm_config=llm_config)

str = 'what is the schedule today'

reply = analyzer.analyze_text(str,'Is there any thing about the assesment or schedule REPLY ONLY YES OR NO ')
