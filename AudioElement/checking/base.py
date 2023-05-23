import requests

endpoint = 'http://localhost:8000/Api/VideoMaker/'

data = {    
			"typee": "video_music",
			"video_component_id": "xyz",
			"high_volume": 50,
			"low_volume": 50,
			"duration": {
                "start_time": 0,
				"end_time": 0,
            },
			"url": ""
}


		# {
		# 	"id": "123",
		# 	"type": "vo",
		# 	"video_component_id": null,
		# 	"high_volume": 100,
		# 	"low_volume": 75,
		# 	"duration": {
		# 		"start_time": 0,
		# 		"end_time": 20
		# 	},
		# 	"url": ""
		# }

result = requests.post(endpoint,json=data)


print(result.json())

print(result.status_code)