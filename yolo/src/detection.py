#!/usr/bin/env python3
from __future__ import print_function

import roslib
#roslib.load_manifest('cvconvert')
import sys
import rospy
import cv2
from std_msgs.msg import String , Float64
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import matplotlib.pyplot as plt
import numpy as np

center_x =0
center_y =0
h=0
w=0
x=0
y=0

yolo=cv2.dnn.readNet("yolov3.weights","yolov3.cfg")
classes=[]

with open("coco.names", 'r') as f:
  classes=f.read().splitlines()


#def __init__(self):
##self.image_pub = rospy.Publisher("image_topic_2",Image)

#self.bridge = CvBridge()
#self.image_sub = rospy.Subscriber("/gazebo_demo/camera/image_raw",Image,self.callback)

def callback(data):
    try:
        cv_image = CvBridge().imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
        print(e)

    (rows,cols,channels) = cv_image.shape
    blob= cv2.dnn.blobFromImage(cv_image, 1/255, (320, 320), (0, 0, 0), swapRB= True, crop= False)
    yolo.setInput(blob)
    output_layers_name= yolo.getUnconnectedOutLayersNames()
    layeroutput= yolo.forward(output_layers_name)
    boxes=[]
    confidences=[]
    class_ids=[]
    #print(" this is layeroutput : ", output_layers_name)
    global center_x
    global center_y
    global h
    global w
    global x
    global y

    for output in layeroutput:
        for detection in output:
            score=detection[5:]
            class_id = np.argmax(score)
            #print("this is cv_image.shape : ", class_id)
            confidence=score[class_id]
            if confidence>0.7:
                   
                center_x= int(detection[0]*cv_image.shape[1])
                center_y= int(detection[1]*cv_image.shape[0])
                w= int(detection[2]*cv_image.shape[1])
                h= int(detection[3]*cv_image.shape[0])

                x=int(center_x -w/2)
                y=int(center_y- h/2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
            
    indexes= cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_PLAIN
    colors= np.random.uniform(0, 255, size = (len(boxes),3))

    if len(indexes)==0 :
        
        cv2.imshow("cv_image", cv_image)
        cv2.waitKey(1)
        print("Nth detected")
        center_x=0
        center_y=0
    else :
        for i in indexes.flatten():

            x, y, w, h= boxes[i]

        label = str(classes[class_ids[i]])
        confi = str(round(confidences[i], 2))
        color=colors[i]
        if label == "person":
                print("CenterX : ",center_x, "; CenterY : ", center_y)
                
                cv2.rectangle(cv_image, (x, y), (x+w, y+h), color, 2)
                cv2.putText(cv_image, label+" "+confi, (x, y+20), font, 2,(255, 255, 255), 2)
        
        cv2.imshow("cv_image", cv_image)
        cv2.waitKey(1)
        print("Sth detected")
    
    


def main(args):
    #ic = image_converter()
    #rospy.init_node('image_converter', anonymous=True)
    #image_sub = rospy.Subscriber("/gazebo_demo/camera/image_raw",Image,callback)
    try:
        pass
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
