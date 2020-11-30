import cv2
import os
import glob
import numpy
# imgLaink = cv2.imread('c:/Users/Axel/Desktop/code/APMBSI/mosaique/BRframe0062.jpg', cv2.IMREAD_UNCHANGED)
# imgLainkResize = cv2.resize(imgLaink, (920,720))
# cv2.imwrite('c:/Users/Axel/Desktop/code/APMBSI/mosaique/newRick.jpg', imgLainkResize )
# imgLaink = cv2.imread('c:/Users/Axel/Desktop/code/APMBSI/mosaique/newRick.jpg', cv2.IMREAD_UNCHANGED)
path = glob.glob("/home/debian/testMosa/data40/*.jpg")
path2 = glob.glob("/home/debian/testMosa/dataVid/*.jpg")

listeImg = []
couleurImg = []


for img in path:
        n = cv2.imread(img)
        listeImg.append(n)
        r = 0
        g = 0
        b = 0
        for i in range(0,40):
                for y in range(0,40):
                        r = r + n[i][y][0]
                        g = g + n[i][y][1]
                        b = b + n[i][y][2]
        r = r/1600
        g = g/1600
        b = b/1600
        couleurImg.append([r,g,b])
idx=0
tabTest = []
for img in path2:
        tabTest.append(img)
tabTest = sorted(tabTest)
lastMosa = []
for nbrImg in range(len(tabTest)):
        print(tabTest[nbrImg])
        tabMosaique = []
        mosaique=numpy.zeros((1440,1840,3))
        imgLaink = cv2.imread(tabTest[nbrImg])
        for x in range(0,36):
                ptitTabMosaique = []
                for y in range(0,46):
                        r=0
                        g=0
                        b=0
                        for xbis in range(0,20):
                                for ybis in range(0,20):
                                        r = r + imgLaink[x*20+xbis][y*20+ybis][0]
                                        g = g + imgLaink[x*20+xbis][y*20+ybis][1]
                                        b = b + imgLaink[x*20+xbis][y*20+ybis][2]
                        r = r/400
                        g = g/400
                        b = b/400 
                        if(len(lastMosa) != 0):
                                testCoul = abs(couleurImg[lastMosa[x][y]][0] - r) + abs(couleurImg[lastMosa[x][y]][1]-g) + abs(couleurImg[lastMosa[x][y]][2]-b)
                                if(testCoul<40):
                                        ptitTabMosaique.append(lastMosa[x][y])
                                else:
                                        average = 0
                                        listeTrouve = []
                                        nbrImg = 0
                                        while len(listeTrouve) < 15:
                                                nbrImg = 0
                                                for nbrImg in range(0,len(couleurImg)-1):
                                                        testAverage = abs(couleurImg[nbrImg][0] - r) + abs(couleurImg[nbrImg][1]-g) + abs(couleurImg[nbrImg][2]-b)
                                                        if(testAverage<average):
                                                                listeTrouve.append(nbrImg)
                                                average = average + 5
                                        imgChoisie = numpy.random.randint(0,len(listeTrouve))
                                        ptitTabMosaique.append(listeTrouve[imgChoisie])

                        else:
                                average = 0
                                listeTrouve = []
                                nbrImg = 0
                                while len(listeTrouve) < 15:
                                        nbrImg = 0
                                        for nbrImg in range(0,len(couleurImg)-1):
                                                testAverage = abs(couleurImg[nbrImg][0] - r) + abs(couleurImg[nbrImg][1]-g) + abs(couleurImg[nbrImg][2]-b)
                                                if(testAverage<average):
                                                        listeTrouve.append(nbrImg)
                                        average = average + 5
                                imgChoisie = numpy.random.randint(0,len(listeTrouve))
                                ptitTabMosaique.append(listeTrouve[imgChoisie])
                tabMosaique.append(ptitTabMosaique)
                        
        # tabMosaique = numpy.loadtxt('c:/Users/Axel/Desktop/code/APMBSI/mosaique/affiche.txt')
        # tabMosaique = numpy.int64(tabMosaique)
        for idx1 in range (0,len(tabMosaique)):
                for idx2 in range (0,len(tabMosaique[idx1])):
                        mosaique[idx1*40:idx1*40+40, idx2*40:idx2*40+40] = listeImg[tabMosaique[idx1][idx2]]
        pathImg = '/home/debian/testMosa/dataPix2/BRframe' + str(int(idx)).zfill(4)+'.jpg'
        cv2.imwrite(pathImg, mosaique)
        lastMosa = tabMosaique

        idx=idx+1

                
