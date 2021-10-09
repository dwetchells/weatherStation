import board
import busio
import time
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
ads.gain = 1


while True:
    time.sleep(0.5)
    chan = AnalogIn(ads, ADS.P0)
    val = int(chan.value / 100)
    print(val)
    windDir = "Not Connected"
    windDeg = 999

    if 0 <= val <= 10:  # 500
        windDir = "N"
        windDeg = 0

    if 10 <= val <= 20:  # 500
        windDir = "NNE"
        windDeg = 22.5

    if 20 <= val <= 30:  # 500
        windDir = "NE"
        windDeg = 45

    if 30 <= val <= 40:  # 250
        windDir = "ENE"
        windDeg = 67.5

    if 40 <= val <= 60:  # 200
        windDir = "E"
        windDeg = 90

    if 60 <= val <= 75:  # 450
        windDir = "ESE"
        windDeg = 112.5

    if 75 <= val <= 85:  # 400
        windDir = "SE"
        windDeg = 135

    if 85 <= val <= 90:  # 500
        windDir = "SSE"
        windDeg = 157.5

    if 90 <= val <= 110:  # 500
        windDir = "S"
        windDeg = 180

    if 110 <= val <= 120:  # 500
        windDir = "SSW"
        windDeg = 202.5

    if 120 <= val <= 135:  # 500
        windDir = "SW"
        windDeg = 225

    if 135 <= val <= 140:  # 500
        windDir = "WSW"
        windDeg = 247.5

    if 140 <= val <= 150:  # 500
        windDir = "W"
        windDeg = 270

    if 150 <= val <= 160:  # 500
        windDir = "WNW"
        windDeg = 292.5

    if 160 <= val <= 180:  # 500
        windDir = "NW"
        windDeg = 315

    if 180 <= val <= 190:  # 1000
        windDir = "NNW"
        windDeg = 337.5

    if 190 <= val <= 230:  # 500
        windDir = "N"
        windDeg = 0

    print("Wind Dir:    ", windDir)
