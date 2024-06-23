import pandas as pd

df_single = pd.read_excel('data/questions.xlsx', sheet_name='single')
df_choose = pd.read_excel('data/questions.xlsx', sheet_name='choose')

import requests
import json
import asyncio
import aiohttp

def chat(chat_id, message, api_key):
    url = "http://192.168.1.110:10005/api/application/chat_message/{chat_id}".format(chat_id=chat_id)

    payload = json.dumps({
    "message": message,
    "re_chat": False,
    "stream": False
    })
    headers = {
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json',
    'AUTHORIZATION': api_key,
    'Accept': '*/*',
    'Host': '192.168.1.110:10005',
    'Connection': 'keep-alive'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
 
    return json.loads(response.text)['data']['content']

def get_chat_id(api_key, app_id):
    url = f"http://192.168.1.110:10005/api/application/{app_id}/chat/open"

    payload={}
    headers = {
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'AUTHORIZATION': api_key,
    'Accept': '*/*',
    'Host': '192.168.1.110:10005',
    'Connection': 'keep-alive'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.text)['data']

async def fetch_responses(i, row, api_key_knowledge, knowledge_app_id, api_key_noknowledge, noknowledge_app_id):
    k_chat_id = await get_chat_id(api_key_knowledge, knowledge_app_id)
    n_chat_id = await get_chat_id(api_key_noknowledge, noknowledge_app_id)
    message = row['q']
    
    async with aiohttp.ClientSession() as session:
        k_response_task = asyncio.create_task(chat(k_chat_id, message, api_key_knowledge))
        n_response_task = asyncio.create_task(chat(n_chat_id, message, api_key_noknowledge))
        
        k_response = await k_response_task
        n_response = await n_response_task
        
        print(k_response)
        print(n_response)
        
        return (i, k_response, n_response)

async def main(df_single, api_key_knowledge, knowledge_app_id, api_key_noknowledge, noknowledge_app_id):
    tasks = []
    for i, row in df_single.iterrows():
        task = fetch_responses(i, row, api_key_knowledge, knowledge_app_id, api_key_noknowledge, noknowledge_app_id)
        tasks.append(task)
        
    results = await asyncio.gather(*tasks)
    
    for i, k_response, n_response in results:
        df_single.at[i, 'answer_k'] = k_response
        df_single.at[i, 'answer_n'] = n_response
        
        
if __name__ == '__main__':
    api_key_knowledge = 'application-9e76341f760156fb8bed8a051ba3ebd1'
    api_key_noknowledge = 'application-65ae0a3bac26ca5bffb5948824ca0847'
    knowledge_app_id = '65a63718-2a34-11ef-b68a-0242ac130004'
    noknowledge_app_id = 'b2dc7004-2b26-11ef-9e64-0242ac130004'
    df_choose['answer_k'] = ''
    df_choose['answer_n'] = ''
    for i in range(0, len(df_choose)):
        k_chat_id = get_chat_id(api_key_knowledge, knowledge_app_id)
        n_chat_id = get_chat_id(api_key_noknowledge, noknowledge_app_id)
        message = '\n以下选择题只给出正确选项的字母就行，其他解释之类的不需要：\n' + df_choose['q'][i] + df_choose['choose'][i]
        k_response = chat(k_chat_id, message, api_key_knowledge)
        n_response = chat(n_chat_id, message, api_key_noknowledge)
        print(k_response)
        print(n_response)
        df_choose.loc[i, 'answer_k'] = k_response
        df_choose.loc[i, 'answer_n'] = n_response
    df_choose.to_excel('data/choose.xlsx', sheet_name='choose', index=False)
    # asyncio.run(main(df_single, api_key_knowledge, knowledge_app_id, api_key_noknowledge, noknowledge_app_id))
    
    # df_single['answer_k'] = ''
    # df_single['answer_n'] = ''
    # for i in range(0, len(df_single)):
    #     k_chat_id = get_chat_id(api_key_knowledge, knowledge_app_id)
    #     n_chat_id = get_chat_id(api_key_noknowledge, noknowledge_app_id)
    #     message = df_single['q'][i]
    #     k_response = chat(k_chat_id, message, api_key_knowledge)
    #     n_response = chat(n_chat_id, message, api_key_noknowledge)
    #     print(k_response)
    #     print(n_response)
    #     df_single.loc[i, 'answer_k'] = k_response
    #     df_single.loc[i, 'answer_n'] = n_response
    # df_single.to_excel('data/questions.xlsx', sheet_name='single', index=False)