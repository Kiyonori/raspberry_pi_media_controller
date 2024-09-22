import analog_digital_converter.GetADS as GetADS
import analog_digital_converter.GetWattage as GetWattage
import os
from dotenv import load_dotenv


def execute() -> list[float]:
    """
    ディスプレイの消費電力をN秒間測定する
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

    ads = GetADS.execute()

    result: list[float] = []

    for i in range(measurement_seconds):
        wattage: float = GetWattage.execute(
            ads,
            pin1,
            pin2,
        )

        result.append(wattage)

    return result


class GetWattageOnDisplay:
    pass
