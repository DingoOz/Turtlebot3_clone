# Turtlebot3_clone
An updated version of the venerable Turtlebot3


If debugging ST3215 servos on Ubuntu then look at this tool:
https://github.com/Kotakku/FT_SCServo_Debug_Qt


# Motor Mode
To put the ST3215 into a continuous rotation mode, set the register "Work Mode" to 1 and then write a value between -4096 and +4096 to Goal Velocity.
