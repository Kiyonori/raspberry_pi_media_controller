from raspberry_pi_media_controller.modules.send_infrared_signals.power_off_media_player import power_off_media_player
from unittest.mock import patch


@patch(
    target='raspberry_pi_media_controller.modules.send_infrared_signals.power_off_media_player.toggle_media_player_power_status',
)
@patch(
    target='raspberry_pi_media_controller.modules.send_infrared_signals.power_off_media_player.get_wattages_on_media_player',
    return_value=[23.4, 56.7, 33.3, 55.5],
)
def test_power_off_media_player_メソッドは_メディアプレイヤーが稼働中に_内部からtoggle_media_player_power_statusメソッドを1度だけ呼ぶこと(
        mock_get_wattages_off_media_player,
        mock_toggle_media_player_power_status,
):
    power_off_media_player()
    mock_toggle_media_player_power_status.assert_called_once()


@patch(
    target='raspberry_pi_media_controller.modules.send_infrared_signals.power_off_media_player.toggle_media_player_power_status',
)
@patch(
    target='raspberry_pi_media_controller.modules.send_infrared_signals.power_off_media_player.get_wattages_on_media_player',
    return_value=[0.4, 0.3, 0.2, 0.4],
)
def test_power_off_media_player_メソッドは_メディアプレイヤーに電源が供給されていない場合は_内部からtoggle_media_player_power_statusメソッドは1度も呼ばれないこと(
        mock_get_wattages_off_media_player,
        mock_toggle_media_player_power_status,

):
    power_off_media_player()
    mock_toggle_media_player_power_status.assert_not_called()
