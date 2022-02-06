#!/usr/bin/python

import numpy as np
from numpy import asarray
from PIL import Image

import cv2
from imutils.video.pivideostream import PiVideoStream
import imutils
import time

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

class VideoCamera(object):
    def __init__(self, flip = False):
        self.vs = PiVideoStream(resolution=(320,240)).start()
        self.flip = flip
        #self.rawCapture = PiRGBArray(camera, size=(640, 480))
        
        time.sleep(2.0)

    def __del__(self):
        self.vs.stop()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def get_frame(self):
        time.sleep(0.3)
        frame = self.flip_if_needed(self.vs.read())
        # grab the frame from the threaded video stream and resize it
        # to have a maximum width of 1000 pixels
        #frame = imutils.resize(frame, width=1000, height=1000)\
                
        #(h, w) = frame.shape[:2]
        #blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (103.93, 116.77, 123.68))

        # pass the blob through the network and obtain the 
        # detections and predictions
        #net.setInput(blob)
        #detections = net.forward()

        #print(type(data))
        # summarize shape
        #print(data.shape)

        # create Pillow image
        #RGBimage = Image.fromarray(data)
        #print(type(RGBimage))
        
        data = asarray(frame)
        gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
        boxes, weights = hog.detectMultiScale(data, winStride=(8,8))
        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
        for (xA, yA, xB, yB) in boxes:
            # display the detected boxes in the colour picture
            cv2.rectangle(data, (xA, yA), (xB, yB),(0, 255, 0), 2)
        #cv2.imshow("Frame", RGBimage);
        #key = cv2.waitKey(1) & 0xFF
        #rawCapture.truncate(0)
        
        
        #if key == ord("q"):
        #   break
        
        
        ret, jpeg = cv2.imencode('.jpg', data)
        #ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()