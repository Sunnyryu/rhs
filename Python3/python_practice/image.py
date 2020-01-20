import os
import shutil
import json
import os.path
import skimage
import time 
#from PIL import Image
import numpy as np
import pandas as pd
from multiprocessing import Pool

def multiprocessing_pool(x):
    #print('value=', x, 'PID=',os.getpid() )
    time.sleep(1)
    return x * x
# annotations
anno_dir = "/home/sunny/Documents/999/annotations/json/"
image_dir = "/home/sunny/Documents/999/annotations/img/"

# anno_dir에 있는 annotations name
directory = os.listdir(anno_dir)

# 결과를 담을 dictionary
result_dict = {}
# json 파일 2개를 반복
for annotation in directory:
    # json 파일 열기
    with open(anno_dir + annotation) as json_file:
        json_data = json.load(json_file)
    category_id_list = []
    # images 안의 값을 꺼내기 위한 for문
    for images in json_data['images']:
        image_id = images['id']
        image_file_name = images['file_name']
        image_flickr_url = images['flickr_url']
        image_width = images['width']
        image_height = images['height']
        # annotations 안의 값을 꺼내기 위한 for문 
        for segments_get in json_data['annotations']:
            if segments_get['image_id'] == image_id:
                segment_info_name = segments_get['file_name']
                for segments_info_id in segments_get['segments_info']:
                    segment_info_id = segments_info_id['id']
                    category_id_ids = segments_info_id['category_id']
                    for categories_get in json_data['categories']:
                        if category_id_ids == categories_get['id']:
                            category_name = categories_get['name']
                            category_id_list.append(category_id_ids)
                            category_id_newlist = sorted(set(category_id_list))
                        else:
                            continue
                # 해당 위치에 같은 이름이 있는지 확인!
                if os.path.isfile(image_dir+segment_info_name):
                    png_information = skimage.data.load(image_dir+segment_info_name)
                    #png_open = Image.open(image_dir+segment_info_name)
                    #png_information = np.array([png_open.getdata()])
                    # diff 차분 함수 , flatnonzero 배열의 index를 구함
                    counts = np.diff(np.r_[0, np.flatnonzero(np.diff(png_information))+1, png_information.size])
                    counts = pd.Series(counts).to_json(orient='values')
                    # 배열이 json에 못들어가니까 이것을 이용할 수 있음
                    RLE = {
                        "counts": counts,
                        "width": image_width,
                        "height": image_height,
                        }
                    segment_info = {
                        "id": segment_info_id,
                        "category_name": category_name,
                        "mask": RLE,
                    }
                    result_dict = {
                        "id": image_id,
                        "file_name": image_file_name,
                        "flickr_url": image_flickr_url,
                        "width": image_width,
                        "height": image_height,
                        "segments_info": segment_info,
                    }
                    #json 파일로 변경
                    json_file_name = segment_info_name.replace('.png', '.json')
                    with open('/home/sunny/Documents/999/png_to_json/' + f'{json_file_name}', 'w') as f:
                        json.dump(result_dict, f)
                else:
                    break
            else:
                continue
#multi processing
if __name__ == '__main__':
    # 직접 사용하거나 임포트 하기 위해 사용
    pool = Pool(10)
    # 10개로 돌림!
    pool.map(multiprocessing_pool, range(0,1000))
    #범위 설정
    pool.close()
    pool.join()

