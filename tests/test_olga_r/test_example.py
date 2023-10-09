import requests

def test_get_by_statu_available():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=available'
    response = requests.get(url=url)
    print(response.json())

def test_get_by_statu_pending():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=pending'
    response = requests.get(url=url)
    print(response.json())
