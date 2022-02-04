#!/usr/bin/env python3
from __future__ import print_function
import rospy
from sensor_msgs.msg import LaserScan , Imu , Image
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf import transformations


# Util imports
import random
import math
import time
import sys

#importing py



import roslib
#roslib.load_manifest('cvconvert')
import sys
import cv2
from std_msgs.msg import String , Float64
from cv_bridge import CvBridge, CvBridgeError
import matplotlib.pyplot as plt
import numpy as np

global center_x
global center_y
global h
global w
global x
global y
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
    print("Hi")
    try:
        cv_image = CvBridge().imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
        print(e)
    print("Bye")
    (rows,cols,channels) = cv_image.shape
    # cv2.imshow("ros",cv_image)
    blob= cv2.dnn.blobFromImage(cv_image, 1/255, (320, 320), (0, 0, 0), swapRB= True, crop= False)
    yolo.setInput(blob)
    output_layers_name= yolo.getUnconnectedOutLayersNames()
    layeroutput= yolo.forward(output_layers_name)
    boxes=[]
    confidences=[]
    class_ids=[]
    #print(" this is layeroutput : ", output_layers_name)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
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
        
        # cv2.imshow("cv_image", cv_image)
        # cv2.waitKey(1)
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
        
        # cv2.imshow("cv_image", cv_image)
        # cv2.waitKey(1)
        print("Sth detected")
    print("khatam")
    try:
            #rospy.Subscriber("/gazebo_demo/camera/image_raw",Image,callback)
            #image_sub = rospy.Subscriber("/gazebo_demo/camera/image_raw",Image,callback)
            
            msg1 = Twist()
            msg2 = Twist()
        
            if center_x !=0 and center_y !=0:
                print(" These are center_x and center_y : ",center_x, center_y, x, y, h, w)
                speed_z = -Kp_rotation*(400- center_x)
                speed_x = -Kp_linear*(300 - h)
            
                msg1.linear.x = speed_x
                msg1.angular.z = speed_z
                pub.publish(msg1)
                rospy.sleep(1)
                pub.publish(msg2)
                
                print("Bot's linear and angular velocity : ", speed_linear_x , speed_angular_z)
            
            elif center_x ==0 and center_y ==0:	
                print("Searching for baby")
                msg1.linear.x = 0
                msg1.angular.z = 0.2
                pub.publish(msg1)
                rospy.sleep(1)
                pub.publish(msg2)
                print(" ye hai center_x and center_y : ",center_x, center_y, x, y, h, w)
                
            
        # msg1 = Twist()
        # positive speed_z value represents clockwise angular velocity of the bot and positive speed_x value represents forward linear velocity of the robot
            
            
    except:
          pass


hz = 20                     # Cycle Frequency
loop_index = 0              # Number of sampling cycles

max_speed = 0.4          # Maximum speed of the robot on meters/seconds
# max_speed = 0.28          # Maximum speed of the robot on meters/seconds
Kp_linear = 0.002                      # Proportional constant for controller
Kd_linear = 0                       # Derivative constant for controller
Ki_linear = 0 

Kp_rotation= 0.001 
Kd_rotation = 0                       # Derivative constant for controller
Ki_rotation = 0                       # Integrabele constant for controller
# Proportional constant for angle controller (just simple P controller)
angle = 1
# 1 for wall on the left side of the robot (-1 for the right side)
direction = -1
x_dist = 0
y_dist = 0

def clbk_twist(msg):
    global speed_linear_x
    global speed_angular_z
    
    speed_linear_x=msg.linear.x
    speed_angular_z= msg.angular.z
    
    #print("ye hai clbk_twist : ")

def clbk_Imu(msg):
    global angular_velocity_z
    global angular_velocity_y
    global linear_acceleration_x
    global linear_acceleration_y
    
    angular_velocity_z = msg.angular_velocity.z
    angular_velocity_y = msg.angular_velocity.y
    
    linear_acceleration_x = msg.linear_acceleration.x
    linear_acceleration_x = msg.linear_acceleration.x
    
    #print("ye hai clbk_Imu : ")
    
def clbk_odom(msg):
    global x_dist
    global y_dist
    global yaw_
    # position
    position_ = msg.pose.pose.position
    # gives x and y distance of the bot
    x_dist = position_.x
    y_dist = position_.y
    
    # yaw
    # convert quaternions to euler angles, only extracting yaw angle for the robot
    quaternion = (
        msg.pose.pose.orientation.x,
        msg.pose.pose.orientation.y,
        msg.pose.pose.orientation.z,
        msg.pose.pose.orientation.w)
    euler = transformations.euler_from_quaternion(quaternion)
    
    yaw_ = euler[2]
    #print(x_dist, y_dist)

def clbk_laser(msg):
    region = {
    'p' : msg.ranges[:],
    }
    # region['p'][0] represents the 0 degree and 0the value start from back and continues in anti-clockwise direction
    #for i in range(360):
      #print(region['p'][i])

def main():
    global center_x
    global center_y
    global h
    global w
    global x
    global y
    
    rospy.init_node('cmd_robot', anonymous=True)
    rospy.Subscriber("/gazebo_demo/camera/image_raw",Image,callback)
    rate = rospy.Rate(50) # 40hz
    rospy.Subscriber('/cmd_vel', Twist, clbk_twist)
    rospy.Subscriber('/odom', Odometry, clbk_odom)
    rospy.Subscriber('/laser/scan', LaserScan, clbk_laser)
    rospy.Subscriber('/imu', Imu, clbk_Imu)
    rospy.spin()
    # while not rospy.is_shutdown():
    
        # try:
        #     #rospy.Subscriber("/gazebo_demo/camera/image_raw",Image,callback)
        #     #image_sub = rospy.Subscriber("/gazebo_demo/camera/image_raw",Image,callback)
            
        #     msg1 = Twist()
        #     msg2 = Twist()
        
        #     if center_x !=0 and center_y !=0:
        #         print(" These are center_x and center_y : ",center_x, center_y, x, y, h, w)
        #         speed_z = -Kp_rotation*(400- center_x)
        #         speed_x = -Kp_linear*(300 - h)
            
        #         msg1.linear.x = speed_x
        #         msg1.angular.z = speed_z
        #         pub.publish(msg1)
        #         rospy.sleep(1)
        #         pub.publish(msg2)
                
        #         print("Bot's linear and angular velocity : ", speed_linear_x , speed_angular_z)
            
        #     elif center_x ==0 and center_y ==0:	
        #         print("Searching for baby")
        #         msg1.linear.x = 0
        #         msg1.angular.z = 0.2
        #         pub.publish(msg1)
        #         rospy.sleep(1)
        #         pub.publish(msg2)
        #         #print(" ye hai center_x and center_y : ",center_x, center_y, x, y, h, w)
                
            
        #msg1 = Twist()
        #positive speed_z value represents clockwise angular velocity of the bot and positive speed_x value represents forward linear velocity of the robot
            
            
        # except:
        #   pass


if __name__ == '__main__':
    main()
