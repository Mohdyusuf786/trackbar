import numpy as np
import cv2 as cv

def nothing(x):#this funcion will print the value of trackbar
    print(x)
#create ablack image
img=np.zeros([300,300,3],np.uint8)
#naming the window
cv.namedWindow('image')#window name in which we want to create trackbar
#now lets create the trackbar gor BGR channel
cv.createTrackbar('B','image',0,255,nothing) #here nothing is a function which we have to define
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('R','image',0,255,nothing)
while(1):
    cv.imshow("image", img)
    k=cv.waitKey(1) & 0xFF
    if k==ord('q'):
        break
    #method to set the position of trackbar
    b = cv.getTrackbarPos('B','image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')

    img[:]=[b,g,r]
#so this was the BGR track bar
cv.destroyAllWindows()

