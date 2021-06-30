# This is a sample Python script.

# Rosbag to process the bag files
import rosbag
# OpenCV2 for saving an image
import cv2
# OS for system
import os
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge
from datetime import datetime, timedelta


def process_message_image(msg_image, time, info_progress ,dir_yes, dir_no):
    bridge = CvBridge()
    if topic_to_read.find("compressed") > 0:
        image = bridge.compressed_imgmsg_to_cv2(msg_image, "passthrough")
    else:
        image = bridge.imgmsg_to_cv2(msg_image, "passthrough")
    date_from_datestamp = str(datetime.utcfromtimestamp(time.to_sec()) + timedelta(hours=2)) #fix the delay of 2 hours
    date_from_datestamp_not_blank = date_from_datestamp.replace(" ", "-")
    save_image(image, date_from_datestamp_not_blank, dir_no)


def save_image(image, name, dir_to_save):
    cv2.imwrite(os.path.join(dir_to_save, "%s.jpg" % name), image)


def create_folders(folders):
    for f in folders:
        if not os.path.exists(f):
            os.makedirs(f)


if __name__ == '__main__':
    #start modifiable parameters
    skip_between_message = 3
    dir_bag_to_read = '/home/adrian/Descargas/bags/SIAR'
    bag_name = 'siar_2018-06-28-09-57-28.bag'
    topic_to_read = "/front/rgb/image_raw/compressed"
    # topic_to_read = "/front_camera/rgb/image"
    # end modifiable parameters
    output_dirpositive = os.path.join(dir_bag_to_read, bag_name.replace(".bag", "-result/yes"))
    output_dirnegative = os.path.join(dir_bag_to_read, bag_name.replace(".bag", "-result/no"))
    create_folders({output_dirpositive, output_dirnegative})
    bag = rosbag.Bag(os.path.join(dir_bag_to_read, bag_name), "r")
    current_message = 0
    total_messages = bag.get_message_count(topic_filters=topic_to_read)

    print("the total number of messages is : %s" % total_messages)
    for topic, msg, t in bag.read_messages(topics=topic_to_read):
        if (current_message % skip_between_message) == 0:
            progress_calculated = "%s of %s" % (current_message, total_messages)
            process_message_image(msg, t, progress_calculated, output_dirpositive, output_dirnegative)
        current_message += 1
    print("the process has finished")
