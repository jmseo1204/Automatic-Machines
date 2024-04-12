from openai import OpenAI
import openai
import json

def ask(api_key:str, prompt:list, history=[]):
    llm = OpenAI(api_key = api_key)
    ans_JSON = []
    
    history += prompt

    respond = llm.chat.completions.create(
        messages= history,
        model="gpt-3.5-turbo",
        #response_format= {"type":"json_object"},
        temperature = 0.5
    )
    history.append({"role":"assistant", "content":respond.choices[0].message.content})
    
    #ans_JSON.append(json.loads(respond.choices[0].message.content or {}))
    #print(history[-1]['content'])
    return history