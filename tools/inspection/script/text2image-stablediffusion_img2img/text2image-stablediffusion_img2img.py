import os.path
import sys

import requests
#
# api_key = sys.argv[1]  # 如果没有api_key这里会传个none字符串
# base_url = sys.argv[2]
base_url = "http://62.234.222.30:31020"
# 如果配置了多个base_url，多个base_url会以逗号分割
# base_url_arr = sys.argv[2].split(',')

url = base_url + "/api/img2img"  # 通过base_url拼接请求的url

payload = {'prompt': 'gray puppy',
           'model_id': 'realvisxlv40v40bakedvae',
           'negative_prompt': '',
           'width': '512',
           'height': '512',
           'samples': '1',
           'num_inference_steps': '20',
           'seed': '-1',
           'lora_model': '',
           'scheduler': '',
           'vae': '',
           'guidance_scale': '5'}
cur_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(cur_path, 'img2img_test.png')
files = [
	('file', ('0adf68f82134a99c3148e1373bbe99d4 (1) (1).jpg',
	          open(file_path, 'rb'), 'image/png'))
]
headers = {}

response = requests.request("POST", url, data=payload, files=files)

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
