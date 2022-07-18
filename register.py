import cv2
import time
import os
from utils.write_text import regist_text
from utils.encode_faces import encode_face
from utils.sound_player import play_sound
  
# variable
TIMER = 3 # countdown 3 sec before capture a picture
MAX_CAPTURED = 3

#path and variable for detection process
DIRECTORY = os.getcwd() 
ENCODINGPATH = os.path.join(DIRECTORY,'users','encodings.pickle') # path to encodings file
USERSFOLDER = os.path.join(DIRECTORY,'users') # users images directory
IMGFOLDER = ""
DETECTIONMETHOD = 'hog' # use 'hog' instead of 'cnn' to detect faces
SOUNDSFOLDER = os.path.join(DIRECTORY,'sounds')

class Register:
    
    def __init__(self):
        pass

    def register(self):
        captured = 0 # the number of pictures we've already captured
        name = ""
        timer = TIMER
        cap = cv2.VideoCapture(0)
        while True:
            name = input("Enter your name: ")
            IMGFOLDER = os.path.join(DIRECTORY,'users',name)
            try: 
                os.makedirs(IMGFOLDER) 
                break # break the loop when user name is valid (not duplicate)
            except OSError as error:
                print(error) 
                print("User's name is duplicate \n please try another name")  

        os.chdir(IMGFOLDER)

        while (True):
            _, frame = cap.read()
            regist_text(frame,captured,"")
            cv2.imshow('Register',frame)

            # check for the key pressed
            k = cv2.waitKey(45)
 
            # set the key for the countdown to begin. Here we set s
            if (k == ord('s')) and (captured < MAX_CAPTURED):
                start = time.time()
                play_sound(os.path.join(SOUNDSFOLDER,'countdown.wav'))
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

            if cv2.waitKey(45) == ord("q") or (captured == MAX_CAPTURED): # stop when we take 6 photos
                break

        cap.release() 
        cv2.destroyAllWindows()

        # save face data
        encode_face(USERSFOLDER,ENCODINGPATH,DETECTIONMETHOD)