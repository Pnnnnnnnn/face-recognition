import cv2

def regist_text(frame,number,countdown):
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.8
    thickness = 1
    text = {
        0:'Please turn "straight" with a "normal" expression',
        1:'Please turn "left" with a "normal" expression',
        2:'Please turn "right" with a "normal" expression',
        3:'Please turn "straight" and "smile"',
        4:'Please turn "left" and "smile"',
        5:'Please turn "right" and "smile"',
    }
    x = get_center(frame,text[number],font,fontScale,thickness)
    cv2.putText(frame,text[number],(x,frame.shape[0]//20),font,fontScale,(0,255,0),thickness)
    cv2.putText(frame,str(countdown),(frame.shape[1]//2,frame.shape[0]//9),font,fontScale,(0,255,0),thickness)

def get_center(img,text,font,fontScale,thickness):
    # get boundary of this text
    textsize = cv2.getTextSize(text, font, fontScale, thickness)[0]

    # get coords based on boundary
    x = (img.shape[1] - textsize[0]) // 2

    return x