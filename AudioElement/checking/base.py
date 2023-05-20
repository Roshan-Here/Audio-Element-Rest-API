import requests

endpoint = 'http://localhost:8000/Api/VideoMaker/'

data = {
    "typee":'vo',
    "high_volume":45,
    "low_volume":12,
    'duration': {
        'start_time':  10,
        'end_time': 50,
    }
}

result = requests.post(endpoint,json=data)


print(result.json())

print(result.status_code)