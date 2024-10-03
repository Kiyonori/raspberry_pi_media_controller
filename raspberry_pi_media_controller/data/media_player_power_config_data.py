from dataclasses import dataclass


@dataclass()
class MediaPlayerPowerConfigData:
    unplugged_wattage: float
    """消費電力がこの値以下は、電源プラグが接続されていません"""

    powered_off_and_signal_can_be_received_wattages: list[float]
    """消費電力がこの範囲内の場合、リモコン操作による電源ONが可能です"""

    powered_on_wattages: list[float]
    """消費電力がこの範囲内の場合、メディアプレイヤーが稼働中であり、リモコン操作による電源OFF操作が可能です"""

    trouble_wattage: float
    """消費電力がこの値以上の場合、メディアプレイヤーが故障しています"""

    def __init__(
            self,
            unplugged_wattage: float,
            powered_off_and_signal_can_be_received_wattages: list[float],
            powered_on_wattages: list[float],
            trouble_wattage: float,
    ):
        self.unplugged_wattage = unplugged_wattage
        self.powered_off_and_signal_can_be_received_wattages = powered_off_and_signal_can_be_received_wattages
        self.powered_on_wattages = powered_on_wattages
        self.trouble_wattage = trouble_wattage
