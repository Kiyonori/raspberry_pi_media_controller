from raspberry_pi_media_controller.enums.display_power_status_enums import DisplayPowerStatusEnum
from raspberry_pi_media_controller.power_on_display_with_attempting import main
from unittest.mock import patch


def test_power_on_display_with_attempting_はディスプレイの電源状態が_POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED_であるとき_内部からtoggle_display_power_statusメソッドを呼び_電源投入を試みること():
    with patch(
            'raspberry_pi_media_controller.power_on_display_with_attempting.toggle_display_power_status'
    ) as mock_toggle_display_power_status:
        with patch(
                'raspberry_pi_media_controller.power_on_display_with_attempting.get_display_power_status'
        ) as mock_get_display_power_status:
            mock_get_display_power_status.side_effect = [
                DisplayPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED,
                DisplayPowerStatusEnum.POWERED_ON,
            ]

            main()
            mock_toggle_display_power_status.assert_called_once()
