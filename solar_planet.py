import cv2

# Read Image
img = cv2.imread("solar-system.jpg")

# Display Colored Image
cv2.imshow("Display Image",img)

# Convert Colored Image To Grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# Display Grayscale Image
cv2.imshow("Grayscale", gray_img)

#print(gray_img)

cv2.waitKey(0)


cv2.putText(img,  
           "Sun"
           (20, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.imwrite("Solar_systemwithname.jpg",img)


