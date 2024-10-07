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


@patch(
    target='raspberry_pi_media_controller.power_on_display.toggle_display_power_status',
)
@patch(
    target='raspberry_pi_media_controller.power_on_display.get_wattages_on_display',
    return_value=[0.4, 0.3, 0.2, 0.4],
)
def test_power_on_display_メソッドは_ディスプレイに電源が供給されていない場合は_内部からtoggle_display_power_statusメソッドは1度も呼ばれないこと(
        mock_get_wattages_on_display,
        mock_toggle_display_power_status,

):
    power_on_display()
    mock_toggle_display_power_status.assert_not_called()


@patch(
    target='raspberry_pi_media_controller.power_on_display.toggle_display_power_status',
)
@patch(
    target='raspberry_pi_media_controller.power_on_display.get_wattages_on_display',
    return_value=[55.0, 160.0, 60.6, 70.7],
)
def test_power_on_display_メソッドは_ディスプレイがすでに稼働中の場合は_内部からtoggle_display_power_statusメソッドは1度も呼ばれないこと(
        mock_get_wattages_on_display,
        mock_toggle_display_power_status,

):
    power_on_display()
    mock_toggle_display_power_status.assert_not_called()


@patch(
    target='raspberry_pi_media_controller.power_on_display.toggle_display_power_status',
)
@patch(
    target='raspberry_pi_media_controller.power_on_display.get_wattages_on_display',
    return_value=[180.0, 190.0, 222.2, 199.9],
)
def test_power_on_display_メソッドは_ディスプレイが異常に電力を消費している場合_内部からtoggle_display_power_statusメソッドは1度も呼ばれないこと(
        mock_get_wattages_on_display,
        mock_toggle_display_power_status,

):
    power_on_display()
    mock_toggle_display_power_status.assert_not_called()
