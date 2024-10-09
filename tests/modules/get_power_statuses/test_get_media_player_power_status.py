import pytest
from raspberry_pi_media_controller.enums.media_player_power_status_enum \
    import MediaPlayerPowerStatusEnum
from raspberry_pi_media_controller.modules.get_power_statuses.get_media_player_power_status \
    import get_media_player_power_status


@pytest.mark.parametrize(
    "wattages",
    [
        [0.4, 0.35, 0.29, 0.1],
        [0.4, 0.4, 0.4, 0.4],
        [0.1, 0.1, 0.1, 0.1],
        [0, 0, 0, 0],
    ]
)
def test_get_media_player_power_status_は意図したとおり_UNPLUGGED_を返すこと(
        wattages: list[float],
):
    result = get_media_player_power_status(wattages)

    assert result is MediaPlayerPowerStatusEnum.UNPLUGGED


@pytest.mark.parametrize(
    "wattages",
    [
        [8.0, 8.0, 8.0, 8.0],
        [12.3, 12.3, 12.3, 12.3],
        [8.0, 12.3, 8.1, 12.2],
        [12.2, 12.2, 12.2, 12.2],
    ]
)
def test_get_media_player_power_status_は意図したとおり_POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED_を返すこと(
        wattages: list[float],
):
    result = get_media_player_power_status(wattages)

    assert result is MediaPlayerPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED


@pytest.mark.parametrize(
    "wattages",
    [
        [23.4, 44.4, 56.7, 55.5],
        [23.4, 23.4, 23.4, 23.4],
        [56.7, 56.7, 56.7, 56.7],
        [56.6, 56.6, 56.6, 56.6],
    ]
)
def test_get_media_player_power_status_は意図したとおり_POWERED_ON_を返すこと(
        wattages: list[float],
):
    result = get_media_player_power_status(wattages)

    assert result is MediaPlayerPowerStatusEnum.POWERED_ON


@pytest.mark.parametrize(
    "wattages",
    [
        [23.4, 23.4, 80.0, 23.4],
        [0.3, 200.0, 0.4, 18.0],
    ]
)
def test_get_media_player_power_status_は意図したとおり_TROUBLE_を返すこと(
        wattages: list[float],
):
    result = get_media_player_power_status(wattages)

    assert result is MediaPlayerPowerStatusEnum.TROUBLE


@pytest.mark.parametrize(
    "wattages",
    [
        [0.4, 2.4, 2.4, 2.4],
        [3.0, 17.0, 17.0, 17.0],
        [20.0, 23.4, 60.0, 12.3],
    ]
)
def test_get_media_player_power_status_は意図したとおり_GLITCHED_を返すこと(
        wattages: list[float],
):
    result = get_media_player_power_status(wattages)

    assert result is MediaPlayerPowerStatusEnum.GLITCHED
