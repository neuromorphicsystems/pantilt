# Pan-tilt

## Flash the Arduino

Install https://github.com/arduino/arduino-cli.

```sh
arduino-cli compile --fqbn arduino:avr:nano:cpu=atmega328 .; arduino-cli upload -v -p /dev/cu.usbserial-1410 -b arduino:avr:nano:cpu=atmega328 .
```

## Use the Python driver

```sh
python3 -m venv .venv
pip install pyserial
# Change the port in example.py
python example.py
```
