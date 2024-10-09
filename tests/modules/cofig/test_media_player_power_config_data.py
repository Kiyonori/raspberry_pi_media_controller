from raspberry_pi_media_controller.data.media_player_power_config_data \
    import MediaPlayerPowerConfigData
from raspberry_pi_media_controller.modules.config.get_media_player_power_config \
    import get_media_player_power_config


def test_get_media_power_config_data_メソッドは意図した値を返してくること():
    dto: MediaPlayerPowerConfigData = get_media_player_power_config()

    assert isinstance(
        dto,
        MediaPlayerPowerConfigData,
    )

    assert type(dto.unplugged_wattage) == float
    assert dto.unplugged_wattage == 0.4

    assert type(dto.powered_off_and_signal_can_be_received_wattages) == list
    assert type(dto.powered_off_and_signal_can_be_received_wattages[0]) == float
    assert type(dto.powered_off_and_signal_can_be_received_wattages[1]) == float
    assert dto.powered_off_and_signal_can_be_received_wattages[0] == 2.4
    assert dto.powered_off_and_signal_can_be_received_wattages[1] == 20.0

    assert type(dto.powered_on_wattages) == list
    assert type(dto.powered_on_wattages[0]) == float
    assert type(dto.powered_on_wattages[1]) == float
    assert dto.powered_on_wattages[0] == 23.4
    assert dto.powered_on_wattages[1] == 56.7

    assert type(dto.trouble_wattage) == float
    assert dto.trouble_wattage == 80.0
