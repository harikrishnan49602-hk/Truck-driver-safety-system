# Truck-driver-safety-system
The  camera detects driver drowsiness using Python and OpenCV. Arduino Uno stops the demo motor and activates the buzzer and vibration alert. A voltage sensor monitors the battery; if voltage drops below a set limit, it alerts the driver to possible battery theft or low battery voltage.
<img width="1024" height="682" alt="image" src="https://github.com/user-attachments/assets/7c9c808f-d324-439b-8d24-f6a1589a8719" />
The laptop webcam captures the driver's face. Python and OpenCV analyze the camera frames to identify possible drowsiness based on eye closure or face absence. Python sends a command to Arduino Uno through USB serial communication.

When drowsiness is detected, Arduino Uno stops the demonstration motor and activates the buzzer and red LED. The system can also activate a separate vibration motor if one is installed.

The voltage sensor measures the battery voltage and sends an analog signal to Arduino Uno. If the voltage remains below a configured threshold, the Arduino activates the yellow LED and buzzer. The SW-420 sensor can provide an additional vibration or tampering warning.

A voltage drop does not prove battery theft. It can also result from battery discharge, electrical loads, or loose connections. Therefore, this system indicates possible low voltage or tampering rather than confirming theft.
