#pip install pillow

import os
import glob
from PIL import Image

### 이미지 일괄 불러오기 확장자 = .JPG 파일 >>> *.JPG
files = glob.glob('C:/Users/girassol/Desktop/KISTI_team_project/labeling_data/korea_pic/*.jpeg')

count=522

for f in files:
    try:
        img = Image.open(f)
        img_resize = img.resize((1000,562), Image.LANCZOS)         ### 이미지 리사이즈 및 필터 설정
        img_resize.save('C:/Users/girassol/Desktop/KISTI_team_project/labeling_data/korea_pic/resize_com/frame%d.JPG' % count)

        print('Saved frame%d.JPG' % count)

        count += 1

    except OSError as e:
        pass


# ###Filter
#
#     - NEAREST

#     - BOX

#     - BILINEAR

#     - HAMMING

#     - BICUBIC

#     - LANCZOS
