import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
a = str(input("Enter circle color"))
cap = cv2.VideoCapture(0)

while True:

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of red color in HSV
    if (a == 'red'):
        lower_red = np.array([160, 50, 50])
        upper_red = np.array([180, 255, 255])
    elif (a == 'green'):
        lower_red = np.array([50, 100, 100])
        upper_red = np.array([70, 255, 255])
    elif (a == 'yellow'):
        lower_red = np.array([20, 100, 100])
        upper_red = np.array([30, 255, 255])
    elif (a == 'white'):
        lower_red = np.array([0, 0, 255])
        upper_red = np.array([255, 255, 255])
    elif(a == 'orange'):
        ower_red = np.array([20, 100, 100])
        upper_red = np.array([30, 255, 255])
    elif(a == 'blue'):
        lower_red = np.array([20, 100, 100])
        upper_red = np.array([30, 255, 255])
    # else:
    #     print("Wrong colour")

    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.boundingRect(mask)
    # we are just adding 2 more channels on the mask so we can stack it along other images
    mask_3 = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    # ewhenuneunfenfen
    # e
    # e
    # e
    # e
    output = frame.copy()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    mask = cv2.medianBlur(mask, 5)

    # Adaptive Guassian Threshold is to detect sharp edges in the Image. For more information Google it.
    mask = cv2.adaptiveThreshold(mask, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 11, 3.5)

    kernel = np.ones((2, 3), np.uint8)
    gray = cv2.erode(mask, kernel, iterations=1)
    # gray = erosion

    gray = cv2.dilate(gray, kernel, iterations=1)
    # gray = dilation

    # get the size of the final image
    # img_size = gray.shape
    # print img_size

    # detect circles in the image
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200, param1=30, param2=45, minRadius=0, maxRadius=1000)
    # print circles

    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle in the image
            # corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            r = str(r)
            a = f'Radius is {r}'
            b = f'Center is ({x},{y})'
            cv2.putText(output, b, (x - 5 + 80, y - 5 + 120), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (255, 255, 255), 4)
            cv2.putText(output, a, (x - 5+10, y - 5+60), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (100, 255, 255),4)
            # time.sleep(0.5)
            print("Column Number: ")
            print(x)
            print("Row Number: ")
            print(y)
            print("Radius is: ")
            print(r)
            print(f"Center is ({x},{y})")
    cv2.imshow('gray',gray)
    cv2.imshow('mask',mask)
    cv2.imshow('mask_3',mask_3)
    # stacking up all three images together
    stacked = np.hstack((mask_3, output, res))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    cv2.imshow('Result', cv2.resize(stacked, None, fx=0.8, fy=0.8))
    
    k = cv2.waitKey(1) & 0xFF
    if k == 's':
        break

cv2.destroyAllWindows()
cap.release()
