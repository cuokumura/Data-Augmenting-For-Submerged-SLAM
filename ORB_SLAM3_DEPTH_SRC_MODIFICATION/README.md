# ORB-SLAM3 Depth-Integration
This is an R&D ORB-SLAM3 extension with the objective of extending ORB-SLAM3's algorithm to facilitate altitude or depth-measuring sensors. 

As of 4/17/2024, this program is unable to properly fuse depth information to ORB-SLAM3.

## Work Done
- A new .cc program is written in HarborStarter/visual-inertial-depth which properly reads from the Aqualoc's depth dataset.
- Source code is modified so that the depth data can be successfully utilized by ORB-SLAM3

## Difficulties
- IMU data is updated at 200 Hz; new image data is captured at 20Hz; depth data is received approximately at 5Hz. ORB-SLAM3's iteration and update cycle is based off the camera's frequency, so it's difficult to figure out how and when to fuse the depth data.

## Work that needs to be done
