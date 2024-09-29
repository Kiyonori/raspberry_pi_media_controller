from adafruit_ads1x15.ads1115 import ADS1115
from raspberry_pi_media_controller.modules.analog_digital_converter.get_channel import get_channel
from raspberry_pi_media_controller.modules.analog_digital_converter.get_rms import get_rms

INTERNAL_RESISTANCE: int = 62
"""電流計 (SCT013-030) 内部に備わっている内部抵抗値"""

CURRENT_RATIO: int = 1800
"""電流計 (SCT013-030) 電流比1800:1"""

ONE_HOUR_SECONDS: int = 3600

SUPPLY_VOLTAGE = 100
"""電流計 (SCT013-030) が測定している電源の供給電圧"""


def get_wattage(
        ads: ADS1115,
        analog_pin_num_1: int,
        analog_pin_num_2: int,
) -> float:
    """
    消費電力を測定
    """

    channel = get_channel(
        ads,
        analog_pin_num_1,
        analog_pin_num_2,
    )

    rms: float = get_rms(channel)
    current: float = (rms / INTERNAL_RESISTANCE) * CURRENT_RATIO
    wattage: float = current * SUPPLY_VOLTAGE

    return wattage
