import requests

from getpass import getpass

endpoint = 'http://127.0.0.1:8000/auth/'
username = input("Enter Your User Name:")
password = getpass("What is Your Password: ")

data = {
    "username" : username,
    "password":password
}
#endpoint = "http://127.0.0.1:8000/api/products/"

get_response = requests.post(endpoint,json=data)

print(get_response.json())

if get_response.status_code ==200:
    token = get_response.json()['token']
    headers={
        "Authorization":f"Bearer {token}"
    }
    
    endpoint = "http://127.0.0.1:8000/api/products/"
    get_response = requests.get(endpoint,headers=headers)
    #print(get_response.json())
    data = get_response.json()
    next_url= data['next']
    res = data['results']
    
    print("Next_url:",next_url)
    print(res)
    