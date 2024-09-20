import adafruit_ads1x15.ads1115
import adafruit_ads1x15.analog_in
from adafruit_ads1x15.analog_in import AnalogIn


def execute(
        ads: adafruit_ads1x15.ads1115,
        analog_input_pin_1: int,
        analog_input_pin_2: int,
) -> adafruit_ads1x15.analog_in.AnalogIn:
    channel = AnalogIn(
        ads,
        analog_input_pin_1,
        analog_input_pin_2,
    )

    return channel


class GetChannel:
    pass
