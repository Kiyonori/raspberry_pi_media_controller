import analog_digital_converter.GetWattageOnMediaPlayer as GetWattageOnMediaPlayer
import statistics


def main() -> None:
    wattage: list[float] = GetWattageOnMediaPlayer.execute()
    print(wattage)

    median: float = statistics.median(wattage)
    print(median)


main()
