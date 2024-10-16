import pytest
from raspberry_pi_media_controller.enums.media_player_power_status_enum \
    import MediaPlayerPowerStatusEnum
from raspberry_pi_media_controller.modules.my_logger.get_last_message_on_power_on_media_player \
    import get_last_message_on_power_on_media_player


@pytest.mark.parametrize(
    "attempt_count, power_status",
    [
        (0, MediaPlayerPowerStatusEnum.UNPLUGGED),
        (1, MediaPlayerPowerStatusEnum.UNPLUGGED),
        (9, MediaPlayerPowerStatusEnum.UNPLUGGED),
        (10, MediaPlayerPowerStatusEnum.UNPLUGGED),
    ],
)
def test_get_last_message_on_power_on_media_player_は試行回数に関係なく_電源が接続されていない場合のメッセージは想定どおりであること(
        attempt_count: int,
        power_status: MediaPlayerPowerStatusEnum,
):
    message: str = get_last_message_on_power_on_media_player(
        attempt_count,
        power_status,
    )

    assert message == 'The media player power plug is unplugged.'
