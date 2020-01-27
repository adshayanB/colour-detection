import cv2
import pandas as pd

#Reading image
img = cv2.imread('/Users/abalendra/PycharmProjects/color-detection/kobe.jpg')

#Global Variables
clicked = False
r = g = b =0

#Reads the csv file with pandas and assignes names to each column
column_name= ['colour','colour_name','hex','R','G','B']
colour_file =pd.read_csv('colors.csv',names=column_name, header=None)

def getColor (r,g,b):
    min=10000
    for i in range(len(colour_file)):
        diff= abs(r-int(colour_file.loc[i,"R"])) + abs(g-int(colour_file.loc[i,'G'])) + abs(b-int(colour_file.loc[i,'B']))
        if diff<=min:
            min=diff
            colour_name=colour_file.loc[i,'colour_name']
    return colour_name

def draw_function (event, x, y, placehold_0, placehold_1):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos,clicked
        clicked =True
        b,g,r = img [y,x]
        b = int(b)
        g = int(g)
        r = int(r)
cv2.namedWindow('Colour Detector')
cv2.setMouseCallback('Colour Detector',draw_function)   #when it detects a mousclick calls draw function


while True:
    cv2.imshow("Colour Detector",img)
    if clicked:
        cv2.rectangle(img, (20,20), (750,60), (b,g,r) , -1)
        text = getColor(r,g,b) + ' R='+str(r) +' G='+str(g)+ ' B='+str(b)
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if r+g+b>=600:
            cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        clicked=False
    if cv2.waitKey(20) &0xFF == 27:
        break
cv2.destroyAllWindows()


