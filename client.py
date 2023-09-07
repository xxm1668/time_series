import requests
import time

# 定义 FastAPI 服务的 URL，包括路径参数
url = 'http://192.168.204.99:8000/trend/44/2/pv'  # 42 是 item_id
_start = time.time()
# 发送 GET 请求
response = requests.get(url)

# 解析响应内容
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")
_end = time.time()
print(_end - _start)
