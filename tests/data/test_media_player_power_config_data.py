from raspberry_pi_media_controller.data.media_player_power_config_data \
    import MediaPlayerPowerConfigData


def test_MediaPlayerPowerConfigData_はData_Transfer_Objectとして機能すること():
    dto = MediaPlayerPowerConfigData(
        unplugged_wattage=0.5,
        powered_off_and_signal_can_be_received_wattages=[1.5, 1.6],
        powered_on_wattages=[12.3, 34.5],
        trouble_wattage=80,
        handling_maximum_number_of_attempts=7,
        handling_waiting_seconds=8,
    )

    assert isinstance(
        dto,
        MediaPlayerPowerConfigData,
    )

    assert dto.unplugged_wattage == 0.5
    assert dto.powered_off_and_signal_can_be_received_wattages == [1.5, 1.6]
    assert dto.powered_on_wattages == [12.3, 34.5]
    assert dto.trouble_wattage == 80
    assert dto.handling_maximum_number_of_attempts == 7
    assert dto.handling_waiting_seconds == 8
