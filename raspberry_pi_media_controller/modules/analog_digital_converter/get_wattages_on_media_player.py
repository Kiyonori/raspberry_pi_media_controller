import os
from raspberry_pi_media_controller.modules.analog_digital_converter.get_ads import get_ads
from raspberry_pi_media_controller.modules.analog_digital_converter.get_wattage import get_wattage
from raspberry_pi_media_controller.modules.my_load_dotenv import my_load_dotenv


def get_wattages_on_media_player() -> list[float]:
    """
    メディアプレイヤーの消費電力をN秒間測定する
    :return: wattages
    :rtype: list[float] N秒間測定した消費電力
    """

    my_load_dotenv()

    pin1: int = int(
        os.environ.get('MEDIA_PLAYER_AMMETER_PIN_PAIR').split(',')[0]
    )

    pin2: int = int(
        os.environ.get('MEDIA_PLAYER_AMMETER_PIN_PAIR').split(',')[1]
    )

    measurement_seconds: int = int(
        os.environ.get('MEDIA_PLAYER_MEASUREMENT_SECONDS')
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
