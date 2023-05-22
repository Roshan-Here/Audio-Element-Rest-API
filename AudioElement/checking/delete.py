import requests

endpoint = 'http://localhost:8000/Api/VideoMaker/2/delete'


result = requests.delete(endpoint)
print(result.status_code)

if result.status_code == 404:
    print(f'{endpoint} is not valid | no valid data available')
    