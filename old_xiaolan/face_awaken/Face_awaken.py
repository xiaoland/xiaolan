# -*- coding: utf-8 -*-

import os
import sys
import cv2
import time
import numpy as np
sys.path.append('/home/pi/old_xiaolan/old_xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
from recorder import recorder


class FaceAwaken(object):

    def __init__(self, token):

        self.face_dir = "/home/pi/old_xiaolan/old_xiaolan/face_awaken/face_dir/"
        self.face_train_date = "/home/pi/old_xiaolan/old_xiaolan/more/haarcascade_frontalface_default.xml"

    def face_sign_in(self):

        """
        人脸注册
        :return:
        """
        baidu_tts.tts("你的名字是什么呢？")
        recorder.record()
        baidu_stt.stt("./voice.wav", self.token)
        baidu_tts.tts("现在开始注册人脸，请将人脸对准摄像头", self.token)
        try:
            os.system("raspistill -o " + self.face_dir + name + ".jpg")
        except:
            baidu_tts.tts("对不起，注册失败", self.token)
        else:
            baidu_tts.tts("注册成功", self.token)

    def video_face_track(self):

        """
        视频流人脸检测
        :return:
        """
        detector = cv2.CascadeClassifier(self.face_train_date)
        cap = cv2.VideoCapture(0)

        while True:
            ret, image = cap.read()
            faces = detector.detectMultiScale(
                gray,
                scaleFactor=1.15,
                minNeighbors=5,
                minSize=(5, 5),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )
            face_num = len(faces)

            print "检测到" + face_num + "个人脸!"

            for (x, y, w, h) in faces:

                cv2.circle(image, ((x + x + w) / 2, (y + y + h) / 2), w / 2, (0, 255, 0), 2)

            cv2.imshow("Find Faces!", image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            else:
                time.sleep(1)

        return face_num

    def face_compare(self, img):

        """
        人脸对比（1：1）
        :param img: 图片
        :return:
        """
        face_locations = face_recognition.face_locations(output)
        face_encodings = face_recognition.face_encodings(output, face_locations)

        # Loop over each face found in the frame to see if it's someone we know.
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = list(face_distance([obama_face_encoding], face_encoding) <= tolerance)
            name = "unknow"

            if match[0]:
                name = "Barack Obama"

            print("I see someone named {}!".format(name))

    def face_encodings(face_image, known_face_locations=None, num_jitters=1):

        """
        人脸加码
        :param face_image: The image that contains one or more faces
        :param known_face_locations: Optional - the bounding boxes of each face if you already know them.
        :param num_jitters: How many times to re-sample the face when calculating encoding. Higher is more accurate, but slower (i.e. 100 is 100x slower)
        :return: A list of 128-dimensional face encodings (one for each face in the image)
        """
        raw_landmarks = _raw_face_landmarks(face_image, known_face_locations, model="small")
        return [np.array(face_encoder.compute_face_descriptor(face_image, raw_landmark_set, num_jitters)) for
                raw_landmark_set in raw_landmarks]

    def face_distance(self, face_encodings, face_to_compare):

        """
        人脸距离
        :param face_to_compare: 对比的人脸
        :param face_encodings
        :return:
        """
        if len(face_encodings) == 0:
            return np.empty((0))

        return np.linalg.norm(face_encodings - face_to_compare, axis=1)

    def face_awaken(self):

        """
        人脸唤醒
        :return:
        """


