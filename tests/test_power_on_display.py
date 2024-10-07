from raspberry_pi_media_controller.power_on_display import power_on_display
from unittest.mock import patch


@patch(
    target='raspberry_pi_media_controller.power_on_display.toggle_display_power_status',
)
@patch(
    target='raspberry_pi_media_controller.power_on_display.get_wattages_on_display',
    return_value=[2.4, 20.0, 2.4, 20],
)
def test_power_on_display_メソッドは_ディスプレイが稼働していない場合に_内部からtoggle_display_power_statusメソッドを1度だけ呼ぶこと(
        mock_get_wattages_on_display,
        mock_toggle_display_power_status,

):
    power_on_display()
    mock_toggle_display_power_status.assert_called_once()
