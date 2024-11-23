
| Number   | TB3 Original          | TB3_clone              | Num    | Cost  | Link                                                                                                                                                                                                                     |
|----------|-----------------------|------------------------|--------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2        | XL430-W250_T          | ST3215                 | 2      | 60    |                                                                                                                                                                                                                          |
| 3        | Plates                | 3D printed             | -      | 25    | (worst scenario: a whole roll of filament)                                                                                                                                                                               |
| 1        | IMU                   | BMI270                 | 1      | 26    | [SparkFun 6DOF IMU Breakout BMI270](https://core-electronics.com.au/sparkfun-6dof-imu-breakout-bmi270-qwiic.html)                                                                                                        |
| 1        | Servo controller      | Waveshare Serial Board | 1      | 9     | [Serial Bus Servo Driver Board](https://core-electronics.com.au/serial-bus-servo-driver-board.html)                                                                                                                      |
| 1        | Battery               | 3S Lipo Battery        | 1      | 15    |                                                                                                                                                                                                                          |
|          |                       | Raspberry PI 4         | 1      | 93    |                                                                                                                                                                                                                          |
| 2        | Wheels                | 3D Printed             | -      | -     |                                                                                                                                                                                                                          |
| 1        | Lidar                 | A1 Slamtec             | 1      | 100   | [AliExpress Lidar](https://www.aliexpress.com/item/32895330424.html)                                                                                                                                                     |
| Multiple | Nuts and bolts        | Nuts and bolts         | -      | 22    | [Step-down Voltage Regulator](https://core-electronics.com.au/5v-34a-step-down-voltage-regulator-d30v30f5.html)                                                                                                          |
| Multiple | USB cables            | USB cables             | -      | 10    |                                                                                                                                                                                                                          |


# Turtlebot3_clone
An updated version of the venerable Turtlebot3


If debugging ST3215 servos on Ubuntu then look at this tool:
https://github.com/Kotakku/FT_SCServo_Debug_Qt


# Motor Mode
To put the ST3215 into a continuous rotation mode, set the register "Work Mode" to 1 and then write a value between -4096 and +4096 to Goal Velocity.
