import os,dlib,glob,numpy
from skimage import io
import cv2
# 1.人脸关键点检测器
predictor_path = "model/shape_predictor_68_face_landmarks.dat"
# 2.人脸识别模型
face_rec_model_path = "model/dlib_face_recognition_resnet_model_v1.dat"
# 3.候选人脸文件夹
faces_folder_path = "candidata_pic"
# 4.需识别的人脸
img_path = "detection.jpg"
# 1.加载正脸检测器
detector = dlib.get_frontal_face_detector()
# 2.加载人脸关键点检测器
sp = dlib.shape_predictor(predictor_path)
# 3. 加载人脸识别模型
facerec = dlib.face_recognition_model_v1(face_rec_model_path)
win = dlib.image_window()
# 候选人脸描述子list
descriptors = []
# 对文件夹下的每一个人脸进行:
# 1.人脸检测
# 2.关键点检测
# 3.描述子提取
for f in glob.glob(os.path.join(faces_folder_path, "*.jpg")):
    print("Processing file: {}".format(f))
    img = io.imread(f)
    win.clear_overlay()
    win.set_image(img)
 # 1.人脸检测
    dets_1 = detector(img, 1)
    print("Number of faces detected: {}".format(len(dets_1)))
    for k, d in enumerate(dets_1):
  # 2.关键点检测
        shape = sp(img, d)
  # 画出人脸区域和和关键点
        win.clear_overlay()
        win.add_overlay(d)
        win.add_overlay(shape)
  # 3.描述子提取，128D向量
        face_descriptor = facerec.compute_face_descriptor(img, shape)
  # 转换为numpy array
        v = numpy.array(face_descriptor)
        descriptors.append(v)
# 对需识别人脸进行同样处理
# 提取描述子，不再注释
img = io.imread(img_path)
dets = detector(img, 1)
dist = []
for k, d in enumerate(dets):
    shape = sp(img, d)
    face_descriptor = facerec.compute_face_descriptor(img, shape)
    d_test = numpy.array(face_descriptor)
 # 计算欧式距离
    for i in descriptors:
        dist_ = numpy.linalg.norm(i-d_test)
        dist.append(dist_)
    for i in dist:
        if i < 0.48:
            a =dist.index(i)
            image = cv2.imread('candidata_pic/text.jpg')
            for k, d in enumerate(dets_1):
                if k == a:
                    print('检测到相同人脸，已在图片中标出！')
                    image = cv2.rectangle(image, (d.left(), d.top()), (d.right(), d.bottom()), (0, 255, 0), 10)
                    cv2.imshow("Find Faces!", image)
                    cv2.imwrite('ceshi3.jpg', image)
        else:
            print('没有检测到相同人脸！')

