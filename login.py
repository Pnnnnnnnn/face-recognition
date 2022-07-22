import cv2
import os
import pickle
from utils.recognize_image import recognize

# variable
ENCODING_PATH = os.path.join(os.getcwd(),'users','encodings.pickle') # path of encodings file
TOLERANCE = 0.4 # indicate how strict the match is. more strict
DETECTION_METHOD = 'hog' # use 'hog' instead of 'cnn' to detect faces

class Login:
    def __init__(self):
        pass

    def login(self):
        # load the known faces and embeddings
        print("[INFO] loading encodings...")
        f = open(ENCODING_PATH, "rb")
        data_pickle = pickle.loads(f.read())
        is_login_ended = False
        cap = cv2.VideoCapture(0)
        print("[INFO] recognizing faces...")
        

        while not is_login_ended:
            _, frame = cap.read()
            names, res = recognize(frame,data_pickle,DETECTION_METHOD,TOLERANCE)
            cv2.imshow('login',res)
            print(names)
            for name in names:
                cv2.destroyAllWindows()
                if(name == 'Unknown'):
                    if(len(names) == 1): # can detect only unknown person
                        print("Sorry, I can't recognize you, please make sure you've already registered")
                        is_login_ended = True # go back to main menu to ask prefer operation from user again
                        break
                    continue
                answer = (input("Are you {} (y/n)".format(name)).lower() == 'y')
                if answer: # User is matched
                    print("Welcome {}".format(name))
                    is_login_ended = True
                    break
            if cv2.waitKey(1) == ord('q'):
                break
        
        f.close()
        cap.release()
        cv2.destroyAllWindows()