import cv2
import os
from utils.recognize_image import recognize

# variable
ENCODING_PATH = os.path.join(os.getcwd(),'users','encodings.pickle') # path of encodings file
TOLERANCE = 0.4 # indicate how strict the match is. more strict
DETECTION_METHOD = 'hog' # use 'hog' instead of 'cnn' to detect faces

class Login:
    def __init__(self):
        pass

    def login(self):
        cap = cv2.VideoCapture(0)

        while True:
            _, frame = cap.read()
            names, res = recognize(frame,ENCODING_PATH,DETECTION_METHOD,TOLERANCE)
            cv2.imshow('login',res)
            print(names)
            if (cv2.waitKey(1) == ord('q')):
                break

        cap.release()
        cv2.destroyAllWindows()