import adafruit_ads1x15.ads1115 as ads1115
import analog_digital_converter.GetADS as GetADS
import analog_digital_converter.GetWattage as GetWattage
import sys
from datetime import datetime


def main() -> None:
    """
    チャンネル1または、チャンネル2の消費電力を測定する
    """

    if sys.argv.__len__() != 2:
        exit(1)

    channel: str = sys.argv[1]
    analog_pin_1: int
    analog_pin_2: int

    match channel:
        case '1':
            analog_pin_1 = ads1115.P0
            analog_pin_2 = ads1115.P1
        case '2':
            analog_pin_1 = ads1115.P2
            analog_pin_2 = ads1115.P3
        case _:
            exit(1)

    ads = GetADS.execute()

    try:
        while True:
            wattage: float = GetWattage.execute(
                ads,
                analog_pin_1,
                analog_pin_2,
            )

            print(
                'Channel: %s, Wattage: %.2f, Timestamp: %s'
                % (
                    channel,
                    wattage,
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                ),
            )

    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    main()
