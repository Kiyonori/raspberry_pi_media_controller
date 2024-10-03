from raspberry_pi_media_controller.modules.config.get_display_power_config \
    import get_display_power_config
from raspberry_pi_media_controller.data.display_power_config_data \
    import DisplayPowerConfigData


def test_get_display_power_config_メソッドは意図した値を返してくること():
    dto: DisplayPowerConfigData = get_display_power_config()

    assert isinstance(
        dto,
        DisplayPowerConfigData,
    )

    assert type(dto.unplugged_wattage) == float
    assert dto.unplugged_wattage == 0.4

    assert type(dto.powered_off_and_signal_can_not_be_received_wattages) == list
    assert type(dto.powered_off_and_signal_can_not_be_received_wattages[0]) == float
    assert type(dto.powered_off_and_signal_can_not_be_received_wattages[1]) == float
    assert dto.powered_off_and_signal_can_not_be_received_wattages[0] == 2.4
    assert dto.powered_off_and_signal_can_not_be_received_wattages[1] == 3.0

    assert type(dto.powered_off_and_signal_can_be_received_wattages) == list
    assert type(dto.powered_off_and_signal_can_be_received_wattages[0]) == float
    assert type(dto.powered_off_and_signal_can_be_received_wattages[1]) == float
    assert dto.powered_off_and_signal_can_be_received_wattages[0] == 17.0
    assert dto.powered_off_and_signal_can_be_received_wattages[1] == 20.0

    assert type(dto.powered_on_wattages) == list
    assert type(dto.powered_on_wattages[0]) == float
    assert type(dto.powered_on_wattages[1]) == float
    assert dto.powered_on_wattages[0] == 55.0
    assert dto.powered_on_wattages[1] == 160.0

    assert type(dto.trouble_wattage) == float
    assert dto.trouble_wattage == 180.0
