import adafruit_ads1x15.ads1115
import adafruit_ads1x15.analog_in
from adafruit_ads1x15.ads1x15 import Mode
from adafruit_ads1x15.analog_in import AnalogIn


def execute(
        ads: adafruit_ads1x15.ads1115,
        analog_input_pin_1: int,
        analog_input_pin_2: int,
        conversion_mode: int = Mode.CONTINUOUS,
        samples_per_second: int = 860,
) -> adafruit_ads1x15.analog_in.AnalogIn:
    # FIXME 繰り返し処理の中で、何度も代入すると正しい値が取得出来ない
    # ads.mode = conversion_mode
    # ads.data_rate = samples_per_second

    channel = AnalogIn(
        ads,
        analog_input_pin_1,
        analog_input_pin_2,
    )

    return channel


class GetChannel:
    pass
