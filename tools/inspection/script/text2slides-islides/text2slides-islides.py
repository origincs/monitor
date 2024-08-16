import sys

import requests

api_key = sys.argv[1]  # 如果没有api_key这里会传个none字符串
base_url = sys.argv[2]
# 如果配置了多个base_url，多个base_url会以逗号分割
# base_url_arr = sys.argv[2].split(',')
url = base_url + "/api/v1/autoppt/outline_stream"  # 通过base_url拼接请求的url

files = {
	'datatype': (None, 'topic'),
	'topic': (None, '写一个关于中国中学生教育现状的ppt')
}

response = requests.request("POST", url, files=files, stream=True)

if response.status_code != 200:
	print(f"fail\tstatus code is {response.status_code}")
else:
	try:
		for chunk in response.iter_content(chunk_size=10240):
			# 处理响应内容
			text = str(chunk, 'utf-8')
		print("success\tok")
	except Exception as e:
		print("fail\tread stream error")
