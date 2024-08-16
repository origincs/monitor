import sys

import requests

api_key = sys.argv[1]  # 如果没有api_key这里会传个none字符串
base_url = sys.argv[2]
# 如果配置了多个base_url，多个base_url会以逗号分割
# base_url_arr = sys.argv[2].split(',')
url = base_url + "/api/text2img"  # 通过base_url拼接请求的url

json_data = {
	"prompt": "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner))",
	"model_id": "hc-anything-v3-vae",
	"negative_prompt": "",
	"width": "128",
	"height": "128",
	"samples": "1",
	"num_inference_steps": "21",
	"seed": "",
	"lora_model": "",
	"scheduler": "UniPCMultistepScheduler",
	"vae": "",
	"guidance_scale": 7.5
}
response = requests.post(url, json=json_data)
if response.status_code != 200:
	print(f"fail\tstatus code is {response.status_code}")
else:
	try:
		response_json = response.json()
		if response_json['code'] != 200 or response_json['message'] != 'ok':
			print(f"fail\t to generate image: {response_json['message']}")
		else:
			print("success\tok")
	except Exception as e:
		print("fail\tdecode json error")
