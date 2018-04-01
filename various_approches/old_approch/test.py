#Keep Coding And change the world and do not forget anything... Not Again..
import cv2,os
#
# ------------ Main
def tesser_image(fileno):
    image = cv2.imread('1.jpg')
    #os.system("tesseract bothonboth.png data")
    #with open("data.txt") as fh:
        #print(fh.read())
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # grayscale
    _,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV) # threshold
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    dilated = cv2.dilate(thresh,kernel,iterations = 25) # dilate
    image,contours,_ = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # get contours


    i=0
    ffinal = open("final"+str(fileno)+".txt","w")
    for contour in contours:
        # get rectangle bounding contour
        [x,y,w,h] = cv2.boundingRect(contour)
        # discard areas that are too large
        #if h>300 and w>300:
        # continue

        # discard areas that are too small
        if h<40 or w<40:
            continue

        # draw rectangle around contour on original image

        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)
        sample = gray[y:y+h,x:x+w]
        sample = cv2.resize(sample,(0,0),fx=5.0,fy=5.0)
        cv2.imwrite("sample.jpg",sample)
        print(i)
        os.system("tesseract sample.jpg data")
        with open("data.txt") as fh:
            data = fh.read()
            ffinal.write(data)
        fh.close()
        i+=1
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ffinal.close()
tesser_image(1)