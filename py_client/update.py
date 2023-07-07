import requests

endpoint = "http://127.0.0.1:8000/api/products/3/update/"

data = {
    "title":"Today Is fun sunday",
    "price":12500
    
}
get_response = requests.put(endpoint,json=data)

print(get_response.json())