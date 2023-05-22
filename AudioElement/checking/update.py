import requests

endpoint = 'http://localhost:8000/Api/VideoMaker/5/update'

data = {
    "typee":'bg_music',
    "high_volume":25,
    "low_volume":26,
    'duration': {
        'start_time':  99,
        'end_time': 123,
    }
}

result = requests.put(endpoint,json=data)


print(result.json())

print(result.status_code)