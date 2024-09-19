import adafruit_ads1x15.ads1115
import board
import busio


def execute() -> adafruit_ads1x15.ads1115.ADS1115:
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = adafruit_ads1x15.ads1115.ADS1115(i2c)

    return ads


class GetADS:
    pass
