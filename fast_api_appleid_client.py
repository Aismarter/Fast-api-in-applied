import json
import requests
import time


# #
# data = {
#   "item": {
#     "content": {
#       "image_path": "/home/sycv_wbk/deployment/image",
#       "image_name": "1PH6723025420538.jpg"
#
#     },
#   }
# }



data = {
  "item": {
      "image_path": "/home/v/workspace/FastAPI/安装与部署/",
      "image_name": "gtgtgtgt.jpg"
  }
}

headers={
    "accept": "application/json",
    "Content-Type": "application/json"
}

print(type(data['item']['image_name']))
response = requests.post(url="http://192.168.96.125:8000/item",json=data,headers=headers)
print(response)
post_data = eval(response.text)
print(post_data)
