from enum import Enum


class DisplayPowerStatusEnum(Enum):
    """
    ディスプレイの電源状態を表すEnum
    """

    POWERED_ON = 'POWERED_ON'
    """ディスプレイの電源がONです"""

    POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED = 'POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED'
    """ディスプレイの電源がOFFであり、赤外線信号の受信が可能です"""

    # TODO この Enum は消すこと
    POWERED_OFF_AND_SIGNAL_CAN_NOT_BE_RECEIVED = 'POWERED_OFF_AND_SIGNAL_CAN_NOT_BE_RECEIVED'
    """ディスプレイの電源がOFFであり、赤外線信号の受信は出来ません"""

    UNPLUGGED = 'UNPLUGGED'
    """電源に接続されていません"""

    GLITCHED = 'GLITCHED'
    """消費電力を検知したものの、ノイズと判定した"""

    TROUBLE = 'TROUBLE'
    """機器の故障"""
