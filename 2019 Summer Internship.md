# 2019 Summer Internship

黄珂邈

## 3D objects detection

### Goals

Detects the cars and pedestrians in the cloud points and uses the bounding boxes to enclose.

### Platforms & Tools

- Kitti

- Autoware / ROS
- PCL
- MATLAB

### Implementation

Use deep learning method to detect the objects in RGB images and project the lidar points to the images and get the corresponding 3D bounding boxes.

#### Problems

1. Do not use deep learning methods with heavy computation workload.
2. Focus on the orientation of the cars.
3. Be robust to occlusion.

#### ROS

The autoware uses ros as the bottom implementation. The launch file specifies the parameters that the node will be launched with. The head file of boxing alogrithm is written as follows:

```c++
class 3dBoxingBound {
    
}
```





