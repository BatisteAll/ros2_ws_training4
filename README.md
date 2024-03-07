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



