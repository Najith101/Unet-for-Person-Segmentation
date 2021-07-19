import cv2
from tensorflow.keras.models import load_model
import numpy as np

model=load_model("model.h5",compile=False)

cap=cv2.VideoCapture(0)


while True:
    ret,frame=cap.read()
    h,w=frame.shape[:2]
    #resize the frame for predicting
    image=cv2.resize(frame,(256,256))

    #preprocessing the inpput
    image=np.array(image,dtype="float32")
    #convert the pixel values from 0 to 1
    image/=255
    image=np.expand_dims(image,axis=0)



    #get the mask for the frame provided
    pred=model.predict(image)
    img=pred[0]
    #convert the mask to BGR
    img=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR))
    #onvert the values between 0 to 255
    mask=(img>0.5)*255.0
    #resize to prdcition to match the shape of the frame
    mask=cv2.resize(mask,(w,h))

    #display the result
    output = ((0.6 * frame) + (0.4 * mask)).astype("uint8")
    cv2.imshow("frame",output)

    #release when esc key is pressed
    if cv2.waitKey(1)&0xFF==27:
        break

cv2.release()
cv2.destroyAllWindows()
