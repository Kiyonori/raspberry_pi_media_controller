from raspberry_pi_media_controller.modules.send_infrared_signals.toggle_display_power_status \
    import toggle_display_power_status
from unittest.mock import patch


@patch('raspberry_pi_media_controller.modules.send_infrared_signals.toggle_display_power_status.subprocess.run')
def test_toggle_display_power_status_メソッドを呼ぶと_内部でsubprocess_runで外部スクリプトを一度だけ呼んでいること(
        mock_subprocess_run
):
    toggle_display_power_status()

    mock_subprocess_run.assert_called_once()
