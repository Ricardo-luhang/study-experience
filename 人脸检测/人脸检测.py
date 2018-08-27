import sys
from imp import reload
import cv2


reload(sys)

# 待检测的图片路径

imagepath = r'text1.jpg'

# 获取训练好的人脸的参数数据，这里直接从GitHub上使用默认值

face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'haarcascade_eye_tree_eyeglasses.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
# 读取图片

image = cv2.imread(imagepath)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 探测图片中的人脸

faces = face_cascade.detectMultiScale(

    gray,

    scaleFactor=1.15,

    minNeighbors=10,

    minSize=(10, 10),

    flags=0
)

print("发现{0}个人脸!".format(len(faces)))
print(faces)

for (x, y, w, h) in faces:
    img = cv2.rectangle(image, (x, y), (x + w, y + w), (0, 255, 0), 10)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 3)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)


    nose = nose_cascade.detectMultiScale(roi_gray, 1.2, 15)
    for (nx, ny, nw, nh) in nose:
        cv2.rectangle(roi_color, (nx, ny), (nx + nw, ny + nh - 20), (0, 255, 0), 2)
    mouth = mouth_cascade.detectMultiScale(roi_gray, 1.5, 15)
    for (mx, my, mw, mh) in mouth:
        cv2.rectangle(roi_color, (mx, my), (mx + mh, my + mw), (0, 255, 0), 2)

cv2.imshow("Find Faces!", image)
cv2.imwrite('result.jpg', image)

cv2.waitKey(0)