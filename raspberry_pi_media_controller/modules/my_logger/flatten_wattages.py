import math


def flatten_wattages(
        wattages: list[float],
        number_of_digits: int = 2,
) -> str:
    """
    消費電力の list[float] の中身の桁数を丸める
    :param wattages: 消費電力
    :type wattages: list[float]
    :param number_of_digits: 小数点以下の桁数
    :type number_of_digits: int
    :return: 消費電力をひとつの str にした文字列
    :rtype: str
    """

    result: list[float] = []

    for wattage in wattages:
        num = math.floor(wattage * 10 ** number_of_digits) / 10 ** number_of_digits
        result.append(num)

    return ','.join(map(str, result))
