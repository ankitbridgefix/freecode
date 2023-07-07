import requests

endpoint = "https://stackoverflow.com/questions/tagged/visual-studio-code?tab=Newest"
endpoint = "http://127.0.0.1:8000/api/products/17/"

get_response = requests.get(endpoint,json={"title":"Abc123","content":"Hellow World","price":"avd65"}) 
#print(get_response.json()['message'])
print(get_response.json())