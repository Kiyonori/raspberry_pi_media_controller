import pytest
from raspberry_pi_media_controller.enums.display_power_status_enums \
    import DisplayPowerStatusEnum
from raspberry_pi_media_controller.modules.my_logger.get_last_message_on_power_off_display \
    import get_last_message_on_power_off_display


@pytest.mark.parametrize(
    "attempt_count, power_status",
    [
        (0, DisplayPowerStatusEnum.UNPLUGGED),
        (1, DisplayPowerStatusEnum.UNPLUGGED),
        (9, DisplayPowerStatusEnum.UNPLUGGED),
        (10, DisplayPowerStatusEnum.UNPLUGGED),
    ],
)
def test_get_last_message_on_power_off_display_は試行回数に関係なく_電源が接続されていない場合のメッセージは想定どおりであること(
        attempt_count: int,
        power_status: DisplayPowerStatusEnum,
):
    message: str = get_last_message_on_power_off_display(
        attempt_count,
        power_status,
    )

    assert message == 'The display power plug is unplugged.'


@pytest.mark.parametrize(
    "attempt_count, power_status",
    [
        (0, DisplayPowerStatusEnum.TROUBLE),
        (1, DisplayPowerStatusEnum.TROUBLE),
        (9, DisplayPowerStatusEnum.TROUBLE),
        (10, DisplayPowerStatusEnum.TROUBLE),
    ],
)
def test_get_last_message_on_power_off_display_は試行回数に関係なく_消費電力の異常を検知した場合のメッセージは想定どおりであること(
        attempt_count: int,
        power_status: DisplayPowerStatusEnum,
):
    message: str = get_last_message_on_power_off_display(
        attempt_count,
        power_status,
    )

    assert message == 'The display power consumption is excessive.'


def test_get_last_message_on_power_off_display_は電源終了しようとした初回に_すでに電源が終了していた場合のメッセージは想定どおりであること():
    message: str = get_last_message_on_power_off_display(
        attempt_count=0,
        power_status=DisplayPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED,
    )

    assert message == 'The display is already powered off.'


@pytest.mark.parametrize(
    "attempt_count, power_status",
    [
        (1, DisplayPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED),
        (2, DisplayPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED),
        (9, DisplayPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED),
        (10, DisplayPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED),
    ],
)
def test_get_last_message_on_power_off_display_試行1回目以上_試行10回目以下で_電源が終了した場合_メッセージは想定どおりであること(
        attempt_count: int,
        power_status: DisplayPowerStatusEnum,
):
    message: str = get_last_message_on_power_off_display(
        attempt_count,
        power_status,
    )

    assert message == 'The display is powered off now.'


@pytest.mark.parametrize(
    "attempt_count",
    [
        11,
        12,
    ],
)
def test_get_last_message_on_power_off_display_試行回数11回目以上はありえないので_電源が終了しなかった旨のメッセージが返ってくること(
        attempt_count: int,
):
    message: str = get_last_message_on_power_off_display(
        attempt_count,
        DisplayPowerStatusEnum.POWERED_ON,
    )

    assert message == 'The system could not turn off the display.'
