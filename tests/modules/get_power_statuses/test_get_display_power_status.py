import pytest
from raspberry_pi_media_controller.enums.display_power_status_enums \
    import DisplayPowerStatusEnum
from raspberry_pi_media_controller.modules.get_power_statuses.get_display_power_status \
    import get_display_power_status


@pytest.mark.parametrize(
    "wattages",
    [
        [0.4, 0.35, 0.29, 0.1],
        [0.4, 0.4, 0.4, 0.4],
        [0.1, 0.1, 0.1, 0.1],
        [0, 0, 0, 0],
    ]
)
def test_get_display_power_status_は意図したとおり_DISCONNECTED_を返すこと(
        wattages: list[float],
):
    result = get_display_power_status(wattages)

    assert result is DisplayPowerStatusEnum.DISCONNECTED


@pytest.mark.parametrize(
    "wattages",
    [
        [2.4, 3.0, 2.41, 2.44],
        [2.4, 2.9, 2.99, 2.401],
        [3.0, 3.0, 3.0, 3.0],
        [2.4, 2.4, 2.4, 2.4],
    ]
)
def test_get_display_power_status_は意図したとおり_POWERED_OFF_AND_SIGNAL_CAN_NOT_BE_RECEIVED_を返すこと(
        wattages: list[float],
):
    result = get_display_power_status(wattages)

    assert result is DisplayPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_NOT_BE_RECEIVED


@pytest.mark.parametrize(
    "wattages",
    [
        [17.0, 17.0, 17.0, 17.0],
        [20.0, 20.0, 20.0, 20.0],
        [17.0, 20.0, 17.1, 19.99],
        [19.99, 19.99, 19.99, 19.99],
    ]
)
def test_get_display_power_status_は意図したとおり_POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED_を返すこと(
        wattages: list[float],
):
    result = get_display_power_status(wattages)

    assert result is DisplayPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED


@pytest.mark.parametrize(
    "wattages",
    [
        [55.0, 65.4, 78.9, 160.0],
        [55.0, 55.0, 55.0, 55.0],
        [160.0, 160.0, 160.0, 160.0],
        [159.99, 159.99, 159.99, 159.99],
    ]
)
def test_get_display_power_status_は意図したとおり_POWERED_ON_を返すこと(
        wattages: list[float],
):
    result = get_display_power_status(wattages)

    assert result is DisplayPowerStatusEnum.POWERED_ON


@pytest.mark.parametrize(
    "wattages",
    [
        [160, 160.1, 160, 160],
        [0.3, 200.0, 0.4, 18.0],
    ]
)
def test_get_display_power_status_は意図したとおり_TROUBLE_を返すこと(
        wattages: list[float],
):
    result = get_display_power_status(wattages)

    assert result is DisplayPowerStatusEnum.TROUBLE


@pytest.mark.parametrize(
    "wattages",
    [
        [0.4, 2.4, 2.4, 2.4],
        [3.0, 17.0, 17.0, 17.0],
        [20.0, 20.0, 55.0, 55.0],
    ]
)
def test_get_display_power_status_は意図したとおり_GLITCHED_を返すこと(
        wattages: list[float],
):
    result = get_display_power_status(wattages)

    assert result is DisplayPowerStatusEnum.GLITCHED
