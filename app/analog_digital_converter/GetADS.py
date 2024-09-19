import adafruit_ads1x15.ads1115
import board
import busio


class GetADS:
    def execute(self) -> adafruit_ads1x15.ads1115.ADS1115:
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = adafruit_ads1x15.ads1115.ADS1115(i2c)

        return ads
