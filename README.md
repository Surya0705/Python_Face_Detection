# Python_Face_Detection
This is a Python Program that Detects Faces in an Image. It uses OpenCV Python Module for this Purpose. To install this in your system just Use the following Command (Assuming that you are on Windows):
```
pip install opencv-python
```
Or if you are on Ubuntu (10.04 LTS which I use) then just type:
```
pip3 install opencv-python
```
Or Install it according to your OS. After Installation follow the Following Instructions:
1. Install the 'haarcascade_frontalface_default.xml' by going to this [Link ](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml).
2. After visiting click on 'Raw':
<img src='Image1.png'><img>
3. Then Right-Click and then choose Save As:
<img src='Image2.png'><img>
4. Then Save the file in Folder you are working within. Give its Path to Program and you are good to go now.
Now in line 6 of [Main.py](Main.py) file give the Image Path and you'll get the Image with faces detected. Below is the screenshot of my Program:
<img src='Code_Screenshot.png'><img>
Note - Instead of giving an Image Path in line 6 you can edit this and use tkinter filedialog so that instead of giving a Path everytime, the tkinter filedialog asks you to Choose the Image. This will make your Program more Interesting.

And Hope that you liked it!
