import requests


try:
    product_id = int(input("Enter Product Id:\n"))
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"

except:
    product_id = None
    print(product_id,"Not valid id")
else:
    get_response = requests.delete(endpoint)

    print(get_response.status_code)