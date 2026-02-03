import requests
from tools import email_operations

url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"

headers = {
    'Authorization': 'Bearer f5166cf4-72bc-40c2-956f-54f15bfce94f',
    'Content-Type': 'application/json'
}

# step 1: handle the user input
messages = input(">>> User: ")
function = {
    "name": "get_email_address_by_username",
    "description": "get the email address of the username",
    "parameters": {"type": "object", "properties": {"username": {"type": "string", "description": "the username of the user"}}}
}
payload = {
    "model": "doubao-seed-1-8-251228",
    "stream": False,
    "messages": [{"role": "user", "content": messages}],
    "tools": [{"type": "function", "function": function}],
    "tool_choice": "auto"
}
response = requests.request("POST", url, headers=headers, json=payload)
print(f"response.text: {response.text}")

# step 2: handle the response
func_response = ""
if "get_email_address_by_username" in response.text:
    func_response = email_operations.get_email_address_by_username("yaohua.li")
    print(f"response of calling get_email_address_by_username: {func_response}")

# step 3: add the function response to the messages
messages += func_response
payload = {
    "model": "doubao-seed-1-8-251228",
    "stream": False,
    "messages": [{"role": "user", "content": messages}],
    "tools": [{"type": "function", "function": {"name": "get_email_address_by_username",
                                                "description": "get the email address of the username"}}],
    "tool_choice": "auto"
}
response = requests.request("POST", url, headers=headers, json=payload)
print(f"response.text: {response.text}")
