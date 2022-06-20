import cv2
import os
from utils.recognize_image import recognize

# variable
encoding_path = os.path.join(os.getcwd(),'users','encodings.pickle')
tolerance = 0.4
detection_method = 'hog'

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    names, res = recognize(frame,encoding_path,detection_method,tolerance) # is_known contain True if program recognize one of the users
    cv2.imshow('login',res)
    print(names)
    if (cv2.waitKey(1) == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()