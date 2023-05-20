import requests

endpoint = ''

result = requests.get(endpoint)


print(result.json())

print(result.status_code)