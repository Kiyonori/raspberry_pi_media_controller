import adafruit_ads1x15.analog_in
from adafruit_ads1x15 import ads1115
from adafruit_ads1x15.analog_in import AnalogIn


def get_channel(
        ads: ads1115,
        analog_input_pin_1: int,
        analog_input_pin_2: int,
) -> AnalogIn:
    channel = AnalogIn(
        ads,
        analog_input_pin_1,
        analog_input_pin_2,
    )

    return channel
