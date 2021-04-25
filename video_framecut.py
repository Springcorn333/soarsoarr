### 터미널 관리자 모드 > 1~3 모두 입력
# 1. pip install opencv-python

# 2. pip install numpy

# 3. pip install matplotlib

# 원하는 영상 파일 경로 +
# 추출된 이미지를 저장할 파일 경로 +
# while문 이미지 리사이즈할 원하는 숫자 3가지만 수정하면 됨!
# 예외처리 안해서 오류나도 사진 파일은 생성됨.



import cv2
import os
import os.path

print(os.getcwd())

vidcap = cv2.VideoCapture('C:/Users/girassol/Desktop/KISTI_team_project/labeling_data/Korea/5.MOV')

count = 0

while(vidcap.isOpened()):
    ret, image = vidcap.read()
    # ex 이미지 사이즈 540x960으로 변경
    image = cv2.resize(image, (960, 540))


    # 30프레임당 하나씩 이미지 추출
    if(int(vidcap.get(1)) % 5 == 0):
        # print('Saved frame number : ' + str(int(vidcap.get(1))))

        cv2.imwrite('C:/Users/girassol/Desktop/KISTI_team_project/labeling_data/Korea/forlabel/frame%d.jpeg' % count, image)

        print('Saved frame%d.jpeg' % count)

        count += 1

vidcap.release()
