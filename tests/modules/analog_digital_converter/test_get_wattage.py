import pytest
from adafruit_ads1x15.ads1115 import ADS1115
from raspberry_pi_media_controller.modules.analog_digital_converter.get_wattage import get_wattage
from raspberry_pi_media_controller.modules.analog_digital_converter.get_ads import get_ads


@pytest.mark.parametrize(
    "analog_input_pin_1, analog_input_pin_2",
    [
        (0, 1),
        (2, 3),
    ]
)
def test_get_wattage_はfloat型の正の値を返すこと(
        analog_input_pin_1: int,
        analog_input_pin_2: int,
):
    ads: ADS1115 = get_ads()
    wattage = get_wattage(
        ads,
        analog_input_pin_1,
        analog_input_pin_2,
    )

    assert type(wattage) is float
    assert wattage > 0
