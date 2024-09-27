import adafruit_ads1x15.ads1115
import board
import busio
from adafruit_ads1x15.ads1x15 import Mode


def get_ads(
        conversion_mode: int = Mode.CONTINUOUS,
        samples_per_second: int = 860,
) -> adafruit_ads1x15.ads1115.ADS1115:
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = adafruit_ads1x15.ads1115.ADS1115(i2c)
    ads.mode = conversion_mode
    ads.data_rate = samples_per_second

    return ads
