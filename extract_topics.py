from rosbag import Bag
import argparse


parser = argparse.ArgumentParser(description='Extract topics from a rosbag in autoware format.')
parser.add_argument('input', type=str,
                    help='input rosbag name')
parser.add_argument('output', type=str,
                    help='output rosbag name')

args = parser.parse_args()

with Bag(args.output,'w') as new_bag:
    for topic, msg, t in Bag(args.input):
        if topic == '/pandar_points':
            new_bag.write('/points_raw', msg, t)
        elif topic == '/fisheye_camera/front/image_color':
            new_bag.write('/image_raw', msg, t)
        elif topic == '/imu':
            new_bag.write('/imu_raw', msg, t)
