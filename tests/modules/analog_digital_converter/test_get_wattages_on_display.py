from raspberry_pi_media_controller.modules.analog_digital_converter.get_wattages_on_display \
    import get_wattages_on_display


def test_get_wattages_on_display_はfloat型のlistを返すこと():
    wattages: list[float] = get_wattages_on_display()

    assert isinstance(wattages, list)
    assert len(wattages) == 4

    for wattage in wattages:
        assert isinstance(wattage, float)
