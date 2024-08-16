import sys
from time import sleep

import requests

api_key = sys.argv[1]  # 如果没有api_key这里会传个none字符串
base_url = sys.argv[2]
# 如果配置了多个base_url，多个base_url会以逗号分割
# base_url_arr = sys.argv[2].split(',')
task_submit_url = base_url + "/api/v1/task/submit"  # 通过base_url拼接请求的url

json_data = {
	"user_id": "image_queue_8za6ci5IGGeO",
	"user_type": "free",
	"task_type": "text2image-sd",
	"task_params": {
		"prompt": "nihao",
		"negative_prompt": "",
		"guidance_scale": 5,
		"model_id": "realisian111",
		"scheduler": "DDPMScheduler",
		"lora_model": "",
		"samples": 1,
		"seed": -1,
		"width": 128,
		"height": 128,
		"num_inference_steps": 20,
		"vae": ""
	}
}
task_submit_response = requests.post(task_submit_url, json=json_data)
if task_submit_response.status_code != 200:
	print(f"fail\ttask_submit_response code is {task_submit_response.status_code}")
else:
	try:
		task_submit_response_json = task_submit_response.json()
		if task_submit_response_json['code'] != 0 or task_submit_response_json['message'] != 'OK':
			print(f"fail\t to generate image: {task_submit_response_json['message']}")
		else:
			task_id = task_submit_response_json['data']['task_id']
			task_get_url = f"{base_url}/api/v1/task/{task_id}"
			while True:
				task_get_response = requests.request("GET", task_get_url)
				if task_get_response.status_code != 200:
					print(f"fail\ttask_get_response code is {task_get_response.status_code}")
				task_get_response_json = task_get_response.json()
				if task_get_response_json['data']['task_status'] == 'COMPLETED':
					break
				sleep(1)
			print("success\tok")
	except Exception as e:
		print("fail\tdecode json error")
