#!/usr/bin/python2.7
 
# Programma test Haar Features
 
import picamera
from SimpleCV import Image
import time

with picamera.PiCamera() as camera:
    facecount = 0
#    while (1):
#    camera.resolution = (640, 480)
#    camera.resolution = (1296, 972) #(2592, 1944)
    camera.resolution = (2592,1944)
    camera.start_preview()
    while (1):
        try:
#            camera.start_preview()
            time.sleep(3)
            print "Capturing image"
            camera.capture('_foto.jpg')
#            camera.stop_preview()
            print "processing"
#            camera.stop_preview()

            foto=Image("_foto.jpg")
#            foto=Image("test3.jpeg")

            print(foto.listHaarFeatures())

            features=foto.findHaarFeatures('face.xml', 1.3, 3)
            if features:
               features.sortArea()  #largest face first
               for face in features:
                   print "Face found at coordinate : " + str(face.coordinates()) + " Area: " + str(face.area())
                   facecount = facecount+1
#                   face.draw() 
                   face.crop().save('face-f_%d.jpg' % facecount)
#               foto.save('foto_%d.jpg' % facecount)
#        else:
#           print "None found" 


#            features=foto.findHaarFeatures('profile.xml', 1.3, 3)
#            if features:
#               features.sortArea() #largest face first
#               for face in features:
#                  print "face profile foud at coord : " + str(face.coordinates()) + " Area : " + str(face.area())
#                  facecount = facecount + 1
##                  face.draw()
#                  face.crop().save('face-p_%d.jpg' % facecount)
##               foto.save('foto_%d.jpg' % facecount)


        except KeyboardInterrupt:
             break;
   
    camera.stop_preview()
#    foto.save('foto1.jpg') 
    
#    foto.show()
#    time.sleep(10)

