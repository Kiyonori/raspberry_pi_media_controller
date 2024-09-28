import pytest
from adafruit_ads1x15 import ads1115
from adafruit_ads1x15.analog_in import AnalogIn
from raspberry_pi_media_controller.modules.analog_digital_converter.get_ads import get_ads
from raspberry_pi_media_controller.modules.analog_digital_converter.get_channel import get_channel
from raspberry_pi_media_controller.modules.analog_digital_converter.get_rms import get_rms


@pytest.mark.parametrize(
    "analog_input_pin_1, analog_input_pin_2",
    [
        (0, 1),
        (2, 3),
    ]
)
def test_get_rms_メソッドは_float型の値を返すこと(
        analog_input_pin_1: int,
        analog_input_pin_2: int,
):
    ads: ads1115 = get_ads()

    channel: AnalogIn = get_channel(
        ads,
        analog_input_pin_1,
        analog_input_pin_2,
    )

    rms_voltage = get_rms(
        channel,
    )

    assert type(rms_voltage) is float
    assert rms_voltage > 0
