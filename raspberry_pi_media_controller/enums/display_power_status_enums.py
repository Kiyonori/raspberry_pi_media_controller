from enum import Enum


class DisplayPowerStatusEnum(Enum):
    """
    ディスプレイの電源状態を表すEnum
    """

    POWERED_ON = 'POWERED_ON'
    """ディスプレイの電源がONです"""

    POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED = 'POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED'
    """ディスプレイの電源がOFFであり、赤外線信号の受信が可能です"""

    POWERED_OFF_AND_SIGNAL_CAN_NOT_BE_RECEIVED = 'POWERED_OFF_AND_SIGNAL_CAN_NOT_BE_RECEIVED'
    """ディスプレイの電源がOFFであり、赤外線信号の受信は出来ません"""

    DISCONNECTED = 'DISCONNECTED'
    """電源に接続されていません"""

    TROUBLE = 'TROUBLE'
    """機器の故障"""
