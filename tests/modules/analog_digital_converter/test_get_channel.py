from adafruit_ads1x15 import ads1115
from adafruit_ads1x15.analog_in import AnalogIn
from raspberry_pi_media_controller.modules.analog_digital_converter.get_ads import get_ads
from raspberry_pi_media_controller.modules.analog_digital_converter.get_channel import get_channel


def test_get_channel_メソッドは_ピン番号０とピン番号１でAnalogIn_インスタンスを返すこと():
    ads: ads1115 = get_ads()

    instance = get_channel(
        ads,
        analog_input_pin_1=0,
        analog_input_pin_2=1,
    )

    assert isinstance(
        instance,
        AnalogIn,
    )


def test_get_channel_メソッドは_ピン番号２とピン番号３でAnalogIn_インスタンスを返すこと():
    ads: ads1115 = get_ads()

    instance = get_channel(
        ads,
        analog_input_pin_1=2,
        analog_input_pin_2=3,
    )

    assert isinstance(
        instance,
        AnalogIn,
    )
