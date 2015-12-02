#!/usr/bin/env python
import rospy
from me495_hw3.srv import WallMeasurement
from turtlesim.msg import Pose
import tf
import random

yval = None
NOISE = 0.1

def posecb(data, br):
    global yval
    yval = data.y
    br.sendTransform((data.x, data.y, 0.0),
                     tf.transformations.quaternion_from_euler(0,0,data.theta),
                     rospy.Time.now(),
                     "turtle_frame",
                     "world")
    return


def measurement_servicecb(request):
    global yval, noise
    return yval + random.gauss(0, noise)


def main():
    global noise
    rospy.init_node("measurement_server", log_level=rospy.INFO)
    br = tf.TransformBroadcaster()
    noise = rospy.get_param("~meas_noise", NOISE)
    rospy.Subscriber("pose", Pose, posecb, callback_args=br)
    meas_server = rospy.Service("measurement", WallMeasurement, measurement_servicecb)
    rospy.spin()
    
if __name__=='__main__':
    main()



