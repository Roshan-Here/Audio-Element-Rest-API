import requests

endpoint = 'http://localhost:8000/Api/VideoMaker/1/detail'



result = requests.get(endpoint)


print(result.json())

print(result.status_code)