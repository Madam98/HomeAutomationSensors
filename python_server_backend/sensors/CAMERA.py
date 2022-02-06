from flask import Flask, render_template, Response, request
from controlcamera import VideoCamera
import time
import threading
import os
import numpy as np
import cv2

pi_camera = VideoCamera(flip=False)      # <-- change flip if pi camera is rotated.
app = Flask(__name__)

@app.route('/')                          # <-- if user visit our website execute def index
def index():
    return render_template('index.html') # <-- you can customze index.html here

def gen(camera):                         # <-- get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera), mimetype='multipart/x-mixed-replace; boundary=frame')

#if __name__ == '__main__':

def startCAMERA():
    app.run(host='192.168.0.30', port='5000', debug=False)

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', debug=False)
