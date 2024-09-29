import os
from dotenv import load_dotenv
from raspberry_pi_media_controller.modules.analog_digital_converter.get_ads import get_ads
from raspberry_pi_media_controller.modules.analog_digital_converter.get_wattage import get_wattage


def get_wattages_on_display() -> list[float]:
    """
    ディスプレイの消費電力をN秒間測定する
    :return: wattages
    :rtype: list[float] N秒間測定した消費電力
    """

    load_dotenv()

    pin1: int = int(
        os.environ.get('DISPLAY_AMMETER_PIN_PAIR').split(',')[0]
    )

    pin2: int = int(
        os.environ.get('DISPLAY_AMMETER_PIN_PAIR').split(',')[1]
    )

    measurement_seconds: int = int(
        os.environ.get('DISPLAY_MEASUREMENT_SECONDS')
    )

    ads = get_ads()

    result: list[float] = []

    for i in range(measurement_seconds):
        wattage: float = get_wattage(
            ads,
            pin1,
            pin2,
        )

        result.append(wattage)

    return result
