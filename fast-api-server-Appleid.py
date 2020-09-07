# 请求正文
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi import Body
from pydantic import BaseModel  # 导入请求模块
import uvicorn
import time
import cv2
import numpy as np

# class Content(BaseModel):
#     image_path:Optional[str] = '/home/sycv_wbk/solar_detection'
#     image_name:Optional[str] =  '1P6723020300262.jpg'
#
# #  创建数据模型
# class Item(BaseModel):
#     task_id: Optional[str] = 'task_id'
#     task_type: Optional[str]
#     callback: Optional[str] = None
#     content:Content
#     timestamp:Optional[str] = 'time.time()'
class Item(BaseModel):
    task_id:str = "task_id"
    task_type:str = "solar_detection"
    callback:str = ""
    image_path:str = ""
    image_name: str = ""



app = FastAPI()



@app.post("/item")
async def read_item( item: Item = Body(..., embed=True)):
    start_datetime= time.time()
    data = jsonable_encoder(item)
    img_path = data["image_path"] + data["image_name"]
    print(type(img_path))
    print(img_path)
    # info = py.process(data)
    img = cv2.imread(img_path)
    # img = cv2.imdecode(np.fromfile(img_path,dtype=np.uint8),-1)
    # file_path_gbk = img_path.encode('gbk')  # unicode转gbk，字符串变为字节数组

    # print(file_path_gbk)
    # img_mat = cv2.imread(file_path_gbk.decode())
    duration = time.time() - start_datetime
    print("duration: ", duration)
    return img.shape



if __name__ == '__main__':
    uvicorn.run(app='fastapi_post_trt:app', host="192.168.96.125", port=8000) #, reload=True, debug=True)


