import cv2 # Importing the OpenCV Module for this Program.

'''You can Download this Classifier here:
https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml'''
a = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # Providing the Program with the Classifier.
b = cv2.imread('Your Image Path') # Giving the OpenCV Path to the Image File.
c = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY) # Converting the Colored image to Gray because the Classifier can only detect in Grayscale Images.

'''Here I have used 1.3 and 3. You can mess up with these values and then 
find out that which one suits the best for you. To know that why I used these 
values just visit this link:
https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php'''
d = a.detectMultiScale(c, 1.3, 3) # Detecting the Faces.

'''Also note that this piece of code between line 19-20 has been used to draw a rectangle
around the detected faces. You'll notice that I have written someting like - "(0, 0, 255), 3"
in line 20. First is BGR Value and 2nd is the Width of Triangle. You may feel free to mess up
with all these values and choose the ones which you like.'''
for (x, y, w, h) in d: # Making the rectangle around the detected faces.
    cv2.rectangle(b, (x, y), (x + w, y + h), (0, 0, 255), 3) # Making the rectangle around the detected faces.

cv2.imshow('Faces Detected', b) # Displaying the detected faces to the User.
cv2.imwrite('Faces Detected.png', b) # This function saves the Detected Faces Image. Just remove out this line if you don't want to save this image.
cv2.waitKey(0) # Waiting for key 0 to be pressed for Program to Exit.
cv2.destroyAllWindows() # Closing all windows one key 0 is Pressed.
