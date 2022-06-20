import os
from utils.encode_faces import encode_face
print("finish import")
  
DIRECTORY = os.getcwd()
ENCODINGPATH = os.path.join(DIRECTORY,'users','encodings.pickle')
IMGFOLDER = ""
DETECTIONMETHOD = 'hog'


encode_face(os.path.join(DIRECTORY,'users'),ENCODINGPATH,DETECTIONMETHOD)