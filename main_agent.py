import requests
from tools import email_operations

url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"

headers = {
    'Authorization': 'Bearer f5166cf4-72bc-40c2-956f-54f15bfce94f',
    'Content-Type': 'application/json'
}

tool_declaration = {
    "type": "function",
    "function": {
        "name": "get_email_address_by_username",
        "description": "get the email address of the username",
        "parameters": {"type": "object", "properties": {"username": {"type": "string", "description": "the username of the user"}}}
    }
}

payload = {
    "model": "deepseek-v3-2-251201",
    "stream": False,
    "messages": [],
    "tools": [tool_declaration]
}

# step 1: LLM handles the user input
messages = input(">>> User: ")
payload["messages"] = [{"role": "user", "content": messages}]
response = requests.request("POST", url, headers=headers, json=payload)
tool_calls = response.json()["choices"][0]["message"]["tool_calls"]
tool_call_id = tool_calls[0]["id"]
assistant_response = response.json()["choices"][0]["message"]["content"]
print(f"<<< raw response: {response.json()}")

# step 2: call the function
tool_response = ""
if "get_email_address_by_username" in response.text:
    tool_response = email_operations.get_email_address_by_username("yaohua.li")
print(f"<<< tool_response: {tool_response}")

# step 3: return the function response to the LLM
payload["messages"] = [{"role": "user", "content": messages},
                       {"role": "assistant", "content": assistant_response, "tool_calls": tool_calls},
                       {"role": "tool", "content": tool_response, "tool_call_id": tool_call_id}]
response = requests.request("POST", url, headers=headers, json=payload)
final_response = response.json()["choices"][0]["message"]["content"]
print(f"<<< final_response: {final_response}")
