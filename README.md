# Autoware YOLOv3 and PointPillars

Author: 黄珂邈  Last update: 2019.9.4

### 1. Install Autoware.AI from Source

See installation tutorial on https://gitlab.com/autowarefoundation/autoware.ai/autoware/wikis/Source-Build for **master** branch build.

```bash
wget -O autoware.ai.repos "https://gitlab.com/autowarefoundation/autoware.ai/autoware/raw/master/autoware.ai.repos?inline=false"
```

### 2. Download ROSBAG

Download ROSBAG files from server.

```bash
sftp dataset@10.20.45.112 
# password: ds#1316
cd 2019-03-24/
get 2019-03-24-16-29_X.bag
```

Extract topics from bags to fit Autoware format.

```bash
python2.7 extract_topics.py in.bag out.bag
```

### 3. Run Autoware

Run ROS and rosbag.

```bash
roscore
```

Source setup file.

```bash
source $HOME/autoware.ai/install/setup.bash
```

Change the settings in **my_launch.launch** file and run it.

```bash
roslaunch my_launch.launch
```

Run Rviz with the configuration file.

```bash
rosrun rviz rviz -d sustech-2019-03-24.rviz
```

Run ROSBAG and see the test result in rviz.

```bash
rosbag play XXX.bag
```

