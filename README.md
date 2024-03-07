# === Tutorial ROS2 - 4 ===


## --------======== Installation ========---------

### URsim

### launch de code

```bash
sudo podman run --rm -it -p 5900:5900 -p 6080:6080 --net ursim_net --ip 192.168.2.77 -e ROBOT_MODEL=UR10 \
  --mount type=volume,source=ursim-gui-cache,target=/ursim/GUI \
  --mount type=volume,source=urcap-build-cache,target=/ursim/.urcaps \
  -v "${HOME}/ursim/programs:/ursim/programs" -v "${HOME}/ursim/urcaps:/urcaps" \
  --name UR10_sim universalrobots/ursim_cb3
```

```bash
ros2 launch ur10_control ur10.launch.py robot_ip:=192.168.2.77 launch_rviz:=true 
```

```bash
ros2 launch ur10_control ur10.launch.py robot_ip:=192.168.2.77 use_fake_hardware:=true launch_rviz:=true 
```



```bash
ros2 topic pub --once /joint_trajectory_controller/joint_trajectory trajectory_msgs/JointTrajectory '{header: {stamp: now, frame_id: "base_link"}, joint_names: ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"], points: [{positions: [1.57, -1.57, 0.0, 0.0, 0.0, 0.0], time_from_start: {sec: 1, nanosec: 0}}]}'
``
