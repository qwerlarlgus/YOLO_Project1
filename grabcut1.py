import cv2
cv2.__version__    # 4.1.2

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('vlcsnap-2021-02-04-10h05m23s567.png', cv2.IMREAD_GRAYSCALE)

#이미지 로드 후 RGB로 변환
image_bgr = cv2.imread('vlcsnap-2021-02-04-10h05m23s567.png')
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# 사각형 좌표: 시작점의 x,y  ,넢이, 너비
rectangle = (253, 92, 200, 253)

# 초기 마스크 생성
mask = np.zeros(image_rgb.shape[:2], np.uint8)

# grabCut에 사용할 임시 배열 생성
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# grabCut 실행
cv2.grabCut(image_rgb, # 원본 이미지
           mask,       # 마스크
           rectangle,  # 사각형
           bgdModel,   # 배경을 위한 임시 배열
           fgdModel,   # 전경을 위한 임시 배열 
           5,          # 반복 횟수
           cv2.GC_INIT_WITH_RECT) # 사각형을 위한 초기화

# 배경인 곳은 0, 그 외에는 1로 설정한 마스크 생성
mask_2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')

# 이미지에 새로운 마스크를 곱행 배경을 제외
image_rgb_nobg = image_rgb * mask_2[:, :, np.newaxis]

# plot
plt.imshow(image_rgb_nobg)
plt.show()

cv2.imwrite('image1.jpg', image_rgb_nobg)

