import cv2
def take_Screenshot():
    videoCaptureObject=cv2.VideoCapture(0)
    result = True 
    while(result):
        ret,frame=videoCaptureObject.read()
        cv2.imwrite("newPicture.jpg",frame)
        resut= False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    print("Photo Capture")
take_Screenshot()