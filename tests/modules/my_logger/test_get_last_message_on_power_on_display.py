import pytest
from raspberry_pi_media_controller.enums.display_power_status_enums \
    import DisplayPowerStatusEnum
from raspberry_pi_media_controller.modules.my_logger.get_last_message_on_power_on_display \
    import get_last_message_on_power_on_display


@pytest.mark.parametrize(
    "attempt_count, power_status",
    [
        (0, DisplayPowerStatusEnum.UNPLUGGED),
        (1, DisplayPowerStatusEnum.UNPLUGGED),
        (9, DisplayPowerStatusEnum.UNPLUGGED),
        (10, DisplayPowerStatusEnum.UNPLUGGED),
    ],
)
def test_get_last_message_on_power_on_display_は試行回数に関係なく_電源が接続されていない場合のメッセージは想定どおりであること(
        attempt_count: int,
        power_status: DisplayPowerStatusEnum,
):
    message: str = get_last_message_on_power_on_display(
        attempt_count,
        power_status,
    )

    assert message == 'The display power plug is unplugged.'
