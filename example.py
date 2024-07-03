import time

import control

pantilt = control.Pantilt("/dev/cu.usbserial-1430")

pantilt.set(pan_degrees=0.0, tilt_degrees=0.0)
time.sleep(1.0)
pantilt.set(pan_degrees=-45.0, tilt_degrees=45.0)
time.sleep(3.0)
