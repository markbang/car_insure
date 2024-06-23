import requests
import json

cookies = {
    '_ga': 'GA1.1.1976540855.1715512173',
    '_ga_T7QHS60L4Q': 'GS1.1.1718000351.5.1.1718000352.0.0.0',
    'ka_sessionid': '8f2055389d11842960ce4215ed69e00b',
    'CSRF-TOKEN': 'CfDJ8CHCUm6ypKVLpjizcZHPE73Y4zjWVd_Nnw_0N62sAlwiarq5fMxmnsyQLXlH2T4VszqkND0Xk4qsXozGzHsqtevPooInwDE3DOCNzVswtw',
    'GCLB': 'CPmxx_ayz8CxdxAD',
    'build-hash': '25329b9ee1e8ff6e9268ed171e37e91972f190cf',
    'ACCEPTED_COOKIES': 'true',
    'recaptcha-ca-t': 'AaGzOmf4tzCJ94fdi3Y1z5fSR0GpnJmJ6WWXOsDaU8nxWEpkvkOQDrvnNpw92gJeUUIHqIzqCYG_fe9xUZDxLtbtvVajRIKHvfWcCp-iZFD5-psVcnhik-cyZ8YuqdJuken0Tbs6gw857rqpctaJcYjasP-cuOHntmw:U=09586d12a0000000',
    'XSRF-TOKEN': 'CfDJ8CHCUm6ypKVLpjizcZHPE707LpY_e7UfifR6bBgN8OBFXk6AqHJ1-8jSLSJdGBEIcbvxeB2-1vCmkBKqE_3JekMLda4K2ugCMVGT7kQGmeh87A',
    'CLIENT-TOKEN': 'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJrYWdnbGUiLCJhdWQiOiJjbGllbnQiLCJzdWIiOiIiLCJuYnQiOiIyMDI0LTA2LTE2VDA3OjQxOjMzLjc5NTU0NjRaIiwiaWF0IjoiMjAyNC0wNi0xNlQwNzo0MTozMy43OTU1NDY0WiIsImp0aSI6IjM3OTczMjcyLTQzODQtNGE2ZS1hODRhLWY0MjI5ODliOTI0ZiIsImV4cCI6IjIwMjQtMDctMTZUMDc6NDE6MzMuNzk1NTQ2NFoiLCJhbm9uIjp0cnVlLCJmZiI6WyJLZXJuZWxzRmlyZWJhc2VMb25nUG9sbGluZyIsIkFsbG93Rm9ydW1BdHRhY2htZW50cyIsIkZyb250ZW5kRXJyb3JSZXBvcnRpbmciLCJEaXNjdXNzaW9uc1JlYWN0aW9ucyIsIkRhdGFzZXRVcGxvYWRlckR1cGxpY2F0ZURldGVjdGlvbiIsIkRhdGFzZXRzTGxtRmVlZGJhY2tDaGlwIiwiTWV0YXN0b3JlQ2hlY2tBZ2dyZWdhdGVGaWxlSGFzaGVzIiwiS01NYXRlcmlhbFVJRGlhbG9nIiwiQWxsUm91dGVzVG9SZWFjdFJvdXRlciJdLCJmZmQiOnsiS2VybmVsRWRpdG9yQXV0b3NhdmVUaHJvdHRsZU1zIjoiMzAwMDAiLCJFbWVyZ2VuY3lBbGVydEJhbm5lciI6Int9IiwiQ2xpZW50UnBjUmF0ZUxpbWl0UXBzIjoiNDAiLCJDbGllbnRScGNSYXRlTGltaXRRcG0iOiI1MDAiLCJGZWF0dXJlZENvbW11bml0eUNvbXBldGl0aW9ucyI6IjYwMDk1LDU0MDAwLDU3MTYzLDgwODc0IiwiQWRkRmVhdHVyZUZsYWdzVG9QYWdlTG9hZFRhZyI6ImRpc2FibGVkIiwiTW9kZWxJZHNBbGxvd0luZmVyZW5jZSI6IjMzMDEsMzUzMyIsIk1vZGVsSW5mZXJlbmNlUGFyYW1ldGVycyI6InsgXCJtYXhfdG9rZW5zXCI6IDEyOCwgXCJ0ZW1wZXJhdHVyZVwiOiAwLjQsIFwidG9wX2tcIjogNSB9IiwiQ29tcGV0aXRpb25NZXRyaWNUaW1lb3V0TWludXRlcyI6IjMwIn0sInBpZCI6ImthZ2dsZS0xNjE2MDciLCJzdmMiOiJ3ZWItZmUiLCJzZGFrIjoiQUl6YVN5QTRlTnFVZFJSc2tKc0NaV1Z6LXFMNjU1WGE1SkVNcmVFIiwiYmxkIjoiMjUzMjliOWVlMWU4ZmY2ZTkyNjhlZDE3MWUzN2U5MTk3MmYxOTBjZiJ9.',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '_ga=GA1.1.1976540855.1715512173; _ga_T7QHS60L4Q=GS1.1.1718000351.5.1.1718000352.0.0.0; ka_sessionid=8f2055389d11842960ce4215ed69e00b; CSRF-TOKEN=CfDJ8CHCUm6ypKVLpjizcZHPE73Y4zjWVd_Nnw_0N62sAlwiarq5fMxmnsyQLXlH2T4VszqkND0Xk4qsXozGzHsqtevPooInwDE3DOCNzVswtw; GCLB=CPmxx_ayz8CxdxAD; build-hash=25329b9ee1e8ff6e9268ed171e37e91972f190cf; ACCEPTED_COOKIES=true; recaptcha-ca-t=AaGzOmf4tzCJ94fdi3Y1z5fSR0GpnJmJ6WWXOsDaU8nxWEpkvkOQDrvnNpw92gJeUUIHqIzqCYG_fe9xUZDxLtbtvVajRIKHvfWcCp-iZFD5-psVcnhik-cyZ8YuqdJuken0Tbs6gw857rqpctaJcYjasP-cuOHntmw:U=09586d12a0000000; XSRF-TOKEN=CfDJ8CHCUm6ypKVLpjizcZHPE707LpY_e7UfifR6bBgN8OBFXk6AqHJ1-8jSLSJdGBEIcbvxeB2-1vCmkBKqE_3JekMLda4K2ugCMVGT7kQGmeh87A; CLIENT-TOKEN=eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJrYWdnbGUiLCJhdWQiOiJjbGllbnQiLCJzdWIiOiIiLCJuYnQiOiIyMDI0LTA2LTE2VDA3OjQxOjMzLjc5NTU0NjRaIiwiaWF0IjoiMjAyNC0wNi0xNlQwNzo0MTozMy43OTU1NDY0WiIsImp0aSI6IjM3OTczMjcyLTQzODQtNGE2ZS1hODRhLWY0MjI5ODliOTI0ZiIsImV4cCI6IjIwMjQtMDctMTZUMDc6NDE6MzMuNzk1NTQ2NFoiLCJhbm9uIjp0cnVlLCJmZiI6WyJLZXJuZWxzRmlyZWJhc2VMb25nUG9sbGluZyIsIkFsbG93Rm9ydW1BdHRhY2htZW50cyIsIkZyb250ZW5kRXJyb3JSZXBvcnRpbmciLCJEaXNjdXNzaW9uc1JlYWN0aW9ucyIsIkRhdGFzZXRVcGxvYWRlckR1cGxpY2F0ZURldGVjdGlvbiIsIkRhdGFzZXRzTGxtRmVlZGJhY2tDaGlwIiwiTWV0YXN0b3JlQ2hlY2tBZ2dyZWdhdGVGaWxlSGFzaGVzIiwiS01NYXRlcmlhbFVJRGlhbG9nIiwiQWxsUm91dGVzVG9SZWFjdFJvdXRlciJdLCJmZmQiOnsiS2VybmVsRWRpdG9yQXV0b3NhdmVUaHJvdHRsZU1zIjoiMzAwMDAiLCJFbWVyZ2VuY3lBbGVydEJhbm5lciI6Int9IiwiQ2xpZW50UnBjUmF0ZUxpbWl0UXBzIjoiNDAiLCJDbGllbnRScGNSYXRlTGltaXRRcG0iOiI1MDAiLCJGZWF0dXJlZENvbW11bml0eUNvbXBldGl0aW9ucyI6IjYwMDk1LDU0MDAwLDU3MTYzLDgwODc0IiwiQWRkRmVhdHVyZUZsYWdzVG9QYWdlTG9hZFRhZyI6ImRpc2FibGVkIiwiTW9kZWxJZHNBbGxvd0luZmVyZW5jZSI6IjMzMDEsMzUzMyIsIk1vZGVsSW5mZXJlbmNlUGFyYW1ldGVycyI6InsgXCJtYXhfdG9rZW5zXCI6IDEyOCwgXCJ0ZW1wZXJhdHVyZVwiOiAwLjQsIFwidG9wX2tcIjogNSB9IiwiQ29tcGV0aXRpb25NZXRyaWNUaW1lb3V0TWludXRlcyI6IjMwIn0sInBpZCI6ImthZ2dsZS0xNjE2MDciLCJzdmMiOiJ3ZWItZmUiLCJzZGFrIjoiQUl6YVN5QTRlTnFVZFJSc2tKc0NaV1Z6LXFMNjU1WGE1SkVNcmVFIiwiYmxkIjoiMjUzMjliOWVlMWU4ZmY2ZTkyNjhlZDE3MWUzN2U5MTk3MmYxOTBjZiJ9.',
    'origin': 'https://www.kaggle.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.kaggle.com/code/sadafpj/insurance-prediction-using-regression/notebook',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-kaggle-build-version': '25329b9ee1e8ff6e9268ed171e37e91972f190cf',
    'x-xsrf-token': 'CfDJ8CHCUm6ypKVLpjizcZHPE707LpY_e7UfifR6bBgN8OBFXk6AqHJ1-8jSLSJdGBEIcbvxeB2-1vCmkBKqE_3JekMLda4K2ugCMVGT7kQGmeh87A',
}
def get_html(author, kernel):
    json_data = {
        'authorUserName': author,
        'kernelSlug': kernel,
        'tab': 'notebook',
    }
    response = requests.post(
        'https://www.kaggle.com/api/i/kernels.LegacyKernelsService/GetKernelViewModel',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    res_json = json.loads(response.text)
    kernel_url = res_json['kernelRun']['renderedOutputUrl']
    kernel_response = requests.get(kernel_url)
    kernel_html = kernel_response.text
    with open(f"notebooks/{author}_{kernel}.html", "w", encoding='utf-8') as f:
        f.write(kernel_html)


import os
from kaggle.api.kaggle_api_extended import KaggleApi

# 初始化 Kaggle API
api = KaggleApi()
api.authenticate()

def download_notebooks(query, max_pages=10):
    page = 5
    while page <= max_pages:
        print(f"Fetching page {page}")
        notebooks = api.kernels_list(search=query, page=page, page_size=20)
        if not notebooks:
            break

        for notebook in notebooks:
            notebook_ref = notebook.ref
            author = notebook.ref.split('/')[0]
            kernel = notebook.ref.split('/')[1]

            # 下载 notebook
            print(f"Downloading {notebook_ref}")
            get_html(author, kernel)
        page += 1

# 下载所有页面的 insurance 相关的 notebooks
download_notebooks(query="insurance", max_pages=100)
