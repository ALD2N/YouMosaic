# Importing all necessary libraries 
import cv2
import os 
  
# Read the video from specified path 
cam = cv2.VideoCapture("/home/debian/testMosa/vid/Rick.mp4") 
try: 
      
    # creating a folder named data 
    if not os.path.exists('/home/debian/testMosa/dataVid'): 
        os.makedirs('/home/debian/testMosa/dataVid') 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# frame 
currentframe = 0

longueur=len(str(int(3000)))
while(True): 
      
    # reading from frame 
    ret,frame = cam.read() 
  
    if ret:
        if currentframe < 3000 :
            # if video is still left continue creating images 
            name = '/home/debian/testMosa/dataVid/BRframe' + str(int(currentframe)).zfill(longueur)+'.jpg'
            print ('Creating...' + name) 
            frame = frame[0:720, 180:1100]
            # writing the extracted images 
            cv2.imwrite(name, frame) 
    
            # increasing counter so that it will 
            # show how many frames are created 
            currentframe += 1
    else: 
        break
  
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 
