import os
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass
class DisplayPowerConfigData:
    disconnected_wattage: float
    """消費電力がこの値以下は、電源プラグが接続されていません"""

    powered_off_and_signal_can_not_be_received_wattages: list[float]
    """消費電力がこの範囲内の場合、リモコン操作による電源ONができません"""

    powered_off_and_signal_can_be_received_wattages: list[float]
    """消費電力がこの範囲内の場合、リモコン操作による電源ONが可能です"""

    powered_on_wattages: list[float]
    """消費電力がこの範囲内の場合、ディスプレイが稼働中であり、リモコン操作による電源OFF操作が可能です"""

    trouble_wattage: float
    """消費電力がこの値以上の場合、ディスプレイが故障しています"""

    def __init__(self):
        # TODO これは DTO に書くべき実装じゃない
        #  DTO はロジックを含んではいけない
        load_dotenv()
        self.disconnected_wattage = float(os.environ.get('DISPLAY_POWER_STATUS_PLUG_DISCONNECTED_WATTAGE'))
        self.powered_off_and_signal_can_not_be_received_wattages = [
            float(
                os
                .environ
                .get('DISPLAY_POWER_STATUS_POWERED_OFF_AND_SIGNAL_CAN_NOT_BE_RECEIVED_WATTAGES')
                .split(',')[0]
            ),
            float(
                os
                .environ
                .get('DISPLAY_POWER_STATUS_POWERED_OFF_AND_SIGNAL_CAN_NOT_BE_RECEIVED_WATTAGES')
                .split(',')[1]
            ),
        ]
        self.powered_off_and_signal_can_be_received_wattages = []
        self.powered_on_wattages = []
        self.trouble_wattage = 0.0
