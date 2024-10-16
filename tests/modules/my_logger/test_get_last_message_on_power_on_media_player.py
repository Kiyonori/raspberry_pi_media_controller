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


@pytest.mark.parametrize(
    "attempt_count, power_status",
    [
        (0, MediaPlayerPowerStatusEnum.TROUBLE),
        (1, MediaPlayerPowerStatusEnum.TROUBLE),
        (9, MediaPlayerPowerStatusEnum.TROUBLE),
        (10, MediaPlayerPowerStatusEnum.TROUBLE),
    ],
)
def test_get_last_message_on_power_on_media_player_は試行回数に関係なく_消費電力の異常を検知した場合のメッセージは想定どおりであること(
        attempt_count: int,
        power_status: MediaPlayerPowerStatusEnum,
):
    message: str = get_last_message_on_power_on_media_player(
        attempt_count,
        power_status,
    )

    assert message == 'The media player power consumption is excessive.'


def test_get_last_message_on_power_on_media_player_は電源投入しようとした初回に_すでに電源が着いていた場合のメッセージは想定どおりであること():
    message: str = get_last_message_on_power_on_media_player(
        attempt_count=0,
        power_status=MediaPlayerPowerStatusEnum.POWERED_ON,
    )

    assert message == 'The media player is already powered on.'


@pytest.mark.parametrize(
    "attempt_count, power_status",
    [
        (1, MediaPlayerPowerStatusEnum.POWERED_ON),
        (2, MediaPlayerPowerStatusEnum.POWERED_ON),
        (9, MediaPlayerPowerStatusEnum.POWERED_ON),
        (10, MediaPlayerPowerStatusEnum.POWERED_ON),
    ],
)
def test_get_last_message_on_power_on_media_player_試行1回目以上_試行10回目以下で_電源が付いた場合_メッセージは想定どおりであること(
        attempt_count: int,
        power_status: MediaPlayerPowerStatusEnum,
):
    message: str = get_last_message_on_power_on_media_player(
        attempt_count,
        power_status,
    )

    assert message == 'The media player is powered on now.'


@pytest.mark.parametrize(
    "attempt_count",
    [
        11,
        12,
    ],
)
def test_get_last_message_on_power_on_media_player_試行回数11回目以上はありえないので_電源が付かなかった旨のメッセージが返ってくること(
        attempt_count: int,
):
    message: str = get_last_message_on_power_on_media_player(
        attempt_count,
        MediaPlayerPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED,
    )

    assert message == 'The system could not turn on the media player.'
