import os
import requests

def send_post_request_with_token(url, email, plan_id):
    token = os.getenv('API_TOKEN')
    if not token:
        print("API_TOKEN环境变量未设置。")
        return

    headers = {
        'Authorization': f'{token}'
    }
    data = {
        'email_prefix': email.split('@')[0],
        'email_suffix': email.split('@')[1],
        'plan_id': plan_id
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            json_response = response.json()
            if json_response['status'] == 'success' and json_response['data'] == True:
                print("操作成功:", json_response['message'], email)
            else:
                print("操作失败:", json_response['message'], email)
        else:
            print("POST请求失败，状态码:", response.status_code, email)
    except Exception as e:
        print("发生异常:", e)

url = 'https://go.ceair.site/api/v1/adminentrance/user/generate'

email_file_path = 'emails.txt'

with open(email_file_path, 'r') as file:
    for line in file:
        email = line.strip()
        send_post_request_with_token(url, email, 13)

