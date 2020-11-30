import cv2
import os
cap=cv2.VideoCapture('/home/debian/testMosa/vid/Rick.mp4')
fps=cap.get(cv2.CAP_PROP_FPS)
path_img = '/home/debian/testMosa/dataPix2/'
print('Création de la vidéo')
liste=sorted(os.listdir(path_img))
frame=cv2.imread(path_img+liste[0])
# print(liste)
h,l,c=frame.shape
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('/home/debian/testMosa/output40.avi',fourcc, fps, (l,h))
for i in range(len(liste)):
    print(liste[i])
    frame=cv2.imread(path_img+liste[i])
    out.write(frame)
print('vidéo créée')
out.release()
