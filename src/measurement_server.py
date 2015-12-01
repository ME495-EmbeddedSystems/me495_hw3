#!/usr/bin/env python
import rospy
from me495_hw3.srv import WallMeasurement
from turtlesim.msg import Pose
import random

yval = None
NOISE = 0.1

def posecb(data):
    global yval
    yval = data.y
    return


def measurement_servicecb(request):
    global yval, noise
    return yval + random.gauss(0, noise)


def main():
    global noise
    rospy.init_node("measurement_server", log_level=rospy.INFO)
    noise = rospy.get_param("~noise", NOISE)
    rospy.Subscriber("pose", Pose, posecb)
    meas_server = rospy.Service("measurement", WallMeasurement, measurement_servicecb)
    rospy.spin()
    
if __name__=='__main__':
    main()



