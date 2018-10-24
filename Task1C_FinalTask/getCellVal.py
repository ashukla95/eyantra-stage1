# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2016)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Task1C
*  Filename: getCellVal.py
*  Version: 1.0.0  
*  Date: October 13, 2016
*  
*  Author: Jayant Solanki, e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
**************************************************************************
"""
# detectCellVal detects the numbers/operatorsm,
# perform respective expression evaluation
# and stores them into the grid_map 
# detectCellVal(img,grid_map)

# Find the number/operators, perform the calculations and store the result into the grid_map
# Return the resultant grid_map
import cv2
import numpy as np
# comment here
def detectCellVal(img_rgb,grid_map):
	#your code here


        
        #finding the contour points of every provided digit
        
        cellcontour=[0,0,0,0,0,0,0,0,0,0,0,0]
        for z in range(12):
                imgpath = 'digits/'+str(z)+'.jpg'
                if z==10:
                        imgpath = 'digits/plus.jpg'
                elif z==11:
                        imgpath = 'digits/minus.jpg'
                im=cv2.imread(imgpath,0)
                img=im[22:85,22:85]
                ret, thresh = cv2.threshold(img, 127, 255,0)
                contours,hierarchy = cv2.findContours(thresh,2,1)
                cellcontour[z] = contours[0]

        
        im2 = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        # dividing test images in grids and finding the contour points of each grid
        
        for i in range(6):
                for j in range(6):
        
                        x = 100*i
                        y = 100*j
                        img2 = im2[x+22:x+85,y+22:y+85]

                        ret, thresh2 = cv2.threshold(img2, 127, 255,0)
                        contours,hierarchy = cv2.findContours(thresh2,2,1)
                        cnt2 = contours[0]
                        # contour matching + storing the object/no in grid map
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

        

        result = [0,0,0,0,0,0]
        #calculating result of each row
        for i in range(6):
                ans = 0
                if(grid_map[i][1]=='+'):
                        ans = ans + (grid_map[i][0] + grid_map[i][2])
                elif(grid_map[i][1]=='-'):
                        ans = ans + (grid_map[i][0] - grid_map[i][2])
                if(grid_map[i][3]=='+'):
                        ans = ans + grid_map[i][4]
                elif(grid_map[i][3]=='-'):
                        ans = ans - grid_map[i][4]
                result[i] = ans
                grid_map[i][5] = result[i]



        
        

        grid_line_x = 7
        grid_line_y = 7
        m=600/(grid_line_x-1)
        n=600/(grid_line_y-1)

        #print the result
        p = 550
        for i in range(6):
                q = i*100+50    
                x = p-m/4
                y = q+n/4
                if(result[i]<0 or result[i]>9):
                        x = p-50
                cv2.putText(img_rgb, str(result[i]), (x, y),cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 4)


       
        return grid_map
