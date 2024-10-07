from raspberry_pi_media_controller.modules.send_infrared_signals.power_off_display import power_off_display
from unittest.mock import patch


@patch(
    target='raspberry_pi_media_controller.modules.send_infrared_signals.power_off_display.toggle_display_power_status',
)
@patch(
    target='raspberry_pi_media_controller.modules.send_infrared_signals.power_off_display.get_wattages_on_display',
    return_value=[55.0, 66.0, 160.0, 155.5],
)
def test_power_off_display_メソッドは_ディスプレイが稼働中に_内部からtoggle_display_power_statusメソッドを1度だけ呼ぶこと(
        mock_get_wattages_off_display,
        mock_toggle_display_power_status,
):
    power_off_display()
    mock_toggle_display_power_status.assert_called_once()
