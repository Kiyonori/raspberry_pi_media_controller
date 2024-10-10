from raspberry_pi_media_controller.data.display_power_config_data \
    import DisplayPowerConfigData


def test_DisplayPowerConfigData_はData_Transfer_Objectとして機能すること():
    dto = DisplayPowerConfigData(
        unplugged_wattage=0.5,
        powered_off_and_signal_can_be_received_wattages=[12.3, 45.6],
        powered_on_wattages=[54.3, 123.4],
        trouble_wattage=200,
        handling_maximum_number_of_attempts=5,
        handling_waiting_seconds=6,
    )

    assert isinstance(
        dto,
        DisplayPowerConfigData,
    )

    assert dto.unplugged_wattage == 0.5
    assert dto.powered_off_and_signal_can_be_received_wattages == [12.3, 45.6]
    assert dto.powered_on_wattages == [54.3, 123.4]
    assert dto.trouble_wattage == 200
    assert dto.handling_maximum_number_of_attempts == 5
    assert dto.handling_waiting_seconds == 6
