import cv2
import numpy as np
cellcontour=[0,0,0,0,0,0,0,0,0,0,0,0]
for z in range(12):
    imgpath = 'digits/'+str(z)+'.jpg'
    if z==10:
        imgpath = 'digits/plus.jpg'
    elif z==11:
        imgpath = 'digits/minus.jpg'
    im=cv2.imread(imgpath,0)
    img=im[22:85,22:85]
    #cv2.imshow('cell',img)
    #cv2.waitKey()
    ret, thresh = cv2.threshold(img, 127, 255,0)
    contours,hierarchy = cv2.findContours(thresh,2,1)
    cellcontour[z] = contours[0]
    cv2.drawContours(img, [cellcontour[z]], 0, (0,0,255), 3)


testinput = 'demo.jpg'

grid_line_x = 7
grid_line_y = 7
grid_map = [ [ 0 for i in range(grid_line_y-1) ] for j in range(grid_line_x-1) ]
im2 = cv2.imread(testinput,0)
#print grid_map
for i in range(6):
    
    for j in range(6):
        
        x = 100*i
        y = 100*j
        img2 = im2[x+22:x+85,y+22:y+85]
        #cv2.imshow('grid',img2)
        #cv2.waitKey()
        ret, thresh2 = cv2.threshold(img2, 127, 255,0)
        contours,hierarchy = cv2.findContours(thresh2,2,1)
        cnt2 = contours[0]
        cv2.drawContours(img2, [cnt2], 0, (0,0,255), 3)
        #cv2.imshow('grid',img2)
        #cv2.waitKey()

        match = -1
        for z in range(12):
            ret = cv2.matchShapes(cnt2,cellcontour[z],1,0.0)
            if (ret == 0.0):
                match = z
        if(match == 10):
            grid_map[i][j] = '+'
        elif(match == 11):
            grid_map[i][j] = '-'
        else:
            grid_map[i][j] = match

        j += 1
    i += 1

#print grid_map
for f in range(6):
    for g in range(6):
        if(grid_map[f][g] == -1):
            grid_map[f][g] =0
            
print grid_map        
        
