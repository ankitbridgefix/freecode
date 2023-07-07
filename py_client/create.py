import requests

endpoint = "http://127.0.0.1:8000/api/products/"
#endpoint = "http://127.0.0.1:8000/api/products/product_m"  # model Mixing
headers={
        "Authorization":"Bearer c2eff4721f4ebb64eb6fbdaa3d70aed690a6744c"
    }

data = {
    "title":"Hellow Ankit test",
    "price":1200
    
}
get_response = requests.post(endpoint,json=data,headers=headers)

print(get_response.json())