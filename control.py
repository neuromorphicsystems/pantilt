import struct
import time

import serial


class Pantilt:
    def __init__(
        self,
        port: str,
        pan_n90: int = 900,
        pan_p90: int = 2100,
        tilt_n90: int = 900,
        tilt_p90: int = 2100,
    ):
        self.serial = serial.Serial(port, baudrate=9600)
        time.sleep(3.0)
        self.pan_n90 = pan_n90
        self.pan_p90 = pan_p90
        self.tilt_n90 = tilt_n90
        self.tilt_p90 = tilt_p90

    def set(self, pan_degrees: float, tilt_degrees: float):
        self.serial.write(
            struct.pack(
                "<H",
                round(
                    (-pan_degrees + 90.0) / 180.0 * (self.pan_p90 - self.pan_n90)
                    + self.pan_n90
                ),
            )
            + struct.pack(
                "<H",
                round(
                    (-tilt_degrees + 90.0) / 180.0 * (self.tilt_p90 - self.tilt_n90)
                    + self.tilt_n90
                ),
            )
        )
        self.serial.flush()
