
![image](https://github.com/user-attachments/assets/fa858a1d-86df-4746-96f0-15c8b5397c2e)

Note the model shown here has many items not included in the base configuration.

# Turtlebot3_clone
An updated version of the venerable Turtlebot3

#Bill of Materials

This is only rough, please send a PR with changes or raise an issue. 

| Number   | TB3_clone              | Num    | Cost  | Link                                                                                                                                                                                                                     |
|----------|------------------------|--------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2        | ST3215                 | 2      | 60    |                                                                                                                                                                                                                          |
| 3        | 3D printed             | -      | 25    | (worst scenario: a whole roll of filament)                                                                                                                                                                               |
| 1        | BMI270                 | 1      | 26    | [SparkFun 6DOF IMU Breakout BMI270](https://core-electronics.com.au/sparkfun-6dof-imu-breakout-bmi270-qwiic.html)                                                                                                        |
| 1        | Waveshare Serial Board | 1      | 9     | [Serial Bus Servo Driver Board](https://core-electronics.com.au/serial-bus-servo-driver-board.html)                                                                                                                      |
| 1        | 3S Lipo Battery        | 1      | 15    |                                                                                                                                                                                                                          |
|          | Raspberry PI 4         | 1      | 93    |                                                                                                                                                                                                                          |
| 2        | 3D Printed Wheels      | -      | -     |                                                                                                                                                                                                                          |
| 1        | A1 Slamtec Lidar       | 1      | 100   | [AliExpress Lidar](https://www.aliexpress.com/item/32895330424.html)                                                                                                                                                     |
| Multiple | Nuts and bolts         | -      | 22    | [Step-down Voltage Regulator](https://core-electronics.com.au/5v-34a-step-down-voltage-regulator-d30v30f5.html)                                                                                                          |
| Multiple | USB cables             | -      | 10    |                                                                                                                                                                                                                          |


# Debugging Servos on Ubuntu
If debugging ST3215 servos on Ubuntu then look at this tool:
https://github.com/Kotakku/FT_SCServo_Debug_Qt

# 3D printed parts
https://www.printables.com/model/243076-turtlebot3-double-waffle-plate


# Motor Mode
To put the ST3215 into a continuous rotation mode, set the register "Work Mode" to 1 and then write a value between -4096 and +4096 to Goal Velocity.
