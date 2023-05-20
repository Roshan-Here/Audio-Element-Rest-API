import requests

endpoint = 'http://localhost:8000/Api/'

result = requests.get(endpoint, json={'check':'hellooo'})


print(result.json())

print(result.status_code)