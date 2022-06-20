import cv2
import time
import os
from utils.write_text import regist_text
from utils.encode_faces import encode_face
print("finish import")
  
timer = 3
captured = 0

cap = cv2.VideoCapture(0)

DIRECTORY = os.getcwd()
ENCODINGPATH = os.path.join(DIRECTORY,'users','encodings.pickle')
USERSFOLDER = os.path.join(DIRECTORY,'users')
IMGFOLDER = ""
DETECTIONMETHOD = 'hog'

valid_name = False
while not valid_name:
    name = input("Enter your name: ")
    IMGFOLDER = os.path.join(DIRECTORY,'users',name)
    try: 
        os.mkdir(IMGFOLDER) 
        valid_name = True
    except OSError as error:
        print(error) 
        print("User's name is duplicate \n please try another name")  

os.chdir(IMGFOLDER)

while (True):

    ret, frame = cap.read()
    regist_text(frame,captured,"")
    cv2.imshow('Register',frame)

    # check for the key pressed
    k = cv2.waitKey(45)
 
    # set the key for the countdown to begin. Here we set s
    if (k == ord('s')) and (captured < 6):
        start = time.time()
        while timer > 0:
            _, frame = cap.read()
            regist_text(frame,captured,timer)
            cv2.imshow('Register',frame)
            cv2.waitKey(45)

            # current time
            cur = time.time()
 
            # Update and keep track of Countdown
            # if time elapsed is one second
            # than decrease the counter
            if cur-start >= 1:
                start = cur
                timer -= 1
        _, pic = cap.read()
        captured += 1
        cv2.imwrite(str(captured)+".jpg",pic) # save a register photo
        timer = 3

    if cv2.waitKey(45) == ord("q") or (captured == 6):#for dev process
        break

cap.release() 
cv2.destroyAllWindows()

# save face data
# os.remove(ENCODINGPATH)
encode_face(USERSFOLDER,ENCODINGPATH,DETECTIONMETHOD)