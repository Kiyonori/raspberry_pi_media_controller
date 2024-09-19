import adafruit_ads1x15.ads1115 as ads1115
import analog_digital_converter.GetRMS as GetRMS
import analog_digital_converter.GetChannel as GetChannel
from adafruit_ads1x15.ads1x15 import Mode
from adafruit_ads1x15.analog_in import AnalogIn
import time


class GetWattage:
    INTERNAL_RESISTANCE: int = 62
    """電流計 (SCT013-030) 内部に備わっている内部抵抗値"""

    CURRENT_RATIO: int = 1800
    """電流計 (SCT013-030) 電流比1800:1"""

    ONE_HOUR_SECONDS: int = 3600

    def execute(self,
                ads: ads1115.ADS1115,
                analog_pin_num_1: int,
                analog_pin_num_2: int,
                conversion_mode: int = Mode.CONTINUOUS,
                samples_per_second: int = 860,
                ) -> float:
        """
        消費電力を測定
        """

        channel: AnalogIn = GetChannel.execute(
            ads,
            analog_pin_num_1,
            analog_pin_num_2,
            conversion_mode,
            samples_per_second,
        )

        start_timestamp: float = time.time()
        rms: float = GetRMS.execute(channel)
        elapsed_seconds: float = time.time() - start_timestamp

        current: float = (rms / GetWattage.INTERNAL_RESISTANCE) * GetWattage.CURRENT_RATIO

        wattage = (current * 100) * elapsed_seconds / GetWattage.ONE_HOUR_SECONDS

        return wattage
