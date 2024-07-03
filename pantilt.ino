#include <Servo.h>

Servo pan;
Servo tilt;
uint8_t index = 0;
uint8_t buffer[4];

void setup() {
    pan.attach(3);
    tilt.attach(5);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0) {
        buffer[index] = (uint8_t)(Serial.read());
        ++index;
        if (index >= 4) {
            pan.writeMicroseconds(*((uint16_t*)buffer));
            tilt.writeMicroseconds(*((uint16_t*)(buffer + 2)));
            index = 0;
        }
    }
}
