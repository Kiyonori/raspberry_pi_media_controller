import adafruit_ads1x15.analog_in
import math
import time


def execute(
        channel: adafruit_ads1x15.analog_in.AnalogIn,
) -> float:
    """
    A/DコンバーターからRMS値を取得する

    :param channel: アナログ入力のピン番号 0, 1, 2, 3
    :type channel: adafruit_ads1x15.analog_in.AnalogIn
    :return RMS値 (電圧V)
    :rtype float
    """

    sum_voltage: float = 0
    counter: int = 0
    start_timestamp: float = time.time()

    # 1秒間測定する
    while time.time() - start_timestamp < 1:
        sum_voltage = sum_voltage + channel.voltage ** 2
        counter += 1

    voltage: float = math.sqrt(sum_voltage / counter)

    return voltage


class GetRMS:
    pass
