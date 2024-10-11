from raspberry_pi_media_controller.enums.display_power_status_enums import DisplayPowerStatusEnum
from raspberry_pi_media_controller.power_on_display_with_attempting import main
from unittest.mock import patch


def test_power_on_display_with_attempting_はディスプレイの電源状態が_POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED_であるとき_内部からtoggle_display_power_statusメソッドを呼び_電源投入を試みること():
    # get_wattages_on_display をモック化して
    # 数秒間の測定なしに、即時に固定のワット数を返すようにして、テストを高速化
    with patch(
            'raspberry_pi_media_controller.power_on_display_with_attempting.get_wattages_on_display'
    ) as mock_get_wattages_on_display:
        mock_get_wattages_on_display.return_value = [30, 30, 30, 30]

        # toggle_display_power_status をモック化して
        # 呼び出し回数をアサート
        with patch(
                'raspberry_pi_media_controller.power_on_display_with_attempting.toggle_display_power_status'
        ) as mock_toggle_display_power_status:
            # get_display_power_status をモック化して、
            # 呼び出し毎にテストの意図に合う値を返す
            with patch(
                    'raspberry_pi_media_controller.power_on_display_with_attempting.get_display_power_status'
            ) as mock_get_display_power_status:
                mock_get_display_power_status.side_effect = [
                    DisplayPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED,
                    DisplayPowerStatusEnum.POWERED_ON,
                ]

                main()
                mock_toggle_display_power_status.assert_called_once()


def test_power_on_display_with_attempting_はディスプレイの電源状態が_すでに_POWERED_ON_であるとき_内部からtoggle_display_power_statusメソッドが一度も呼ばれないこと():
    # get_wattages_on_display をモック化して
    # 数秒間の測定なしに、即時に固定のワット数を返すようにして、テストを高速化
    with patch(
            'raspberry_pi_media_controller.power_on_display_with_attempting.get_wattages_on_display'
    ) as mock_get_wattages_on_display:
        mock_get_wattages_on_display.return_value = [30, 30, 30, 30]

        # toggle_display_power_status をモック化して
        # 呼び出し回数をアサート
        with patch(
                'raspberry_pi_media_controller.power_on_display_with_attempting.toggle_display_power_status'
        ) as mock_toggle_display_power_status:
            # get_display_power_status をモック化して、
            # 呼び出し毎にテストの意図に合う値を返す
            with patch(
                    'raspberry_pi_media_controller.power_on_display_with_attempting.get_display_power_status'
            ) as mock_get_display_power_status:
                mock_get_display_power_status.side_effect = [
                    DisplayPowerStatusEnum.POWERED_ON,
                ]

                main()
                mock_toggle_display_power_status.assert_not_called()


def test_power_on_display_with_attempting_はディスプレイに電源が接続されていない_UNPLUGGED_の場合_内部からtoggle_display_power_statusメソッドが一度も呼ばれないこと():
    # get_wattages_on_display をモック化して
    # 数秒間の測定なしに、即時に固定のワット数を返すようにして、テストを高速化
    with patch(
            'raspberry_pi_media_controller.power_on_display_with_attempting.get_wattages_on_display'
    ) as mock_get_wattages_on_display:
        mock_get_wattages_on_display.return_value = [30, 30, 30, 30]

        # toggle_display_power_status をモック化して
        # 呼び出し回数をアサート
        with patch(
                'raspberry_pi_media_controller.power_on_display_with_attempting.toggle_display_power_status'
        ) as mock_toggle_display_power_status:
            # get_display_power_status をモック化して、
            # 呼び出し毎にテストの意図に合う値を返す
            with patch(
                    'raspberry_pi_media_controller.power_on_display_with_attempting.get_display_power_status'
            ) as mock_get_display_power_status:
                mock_get_display_power_status.side_effect = [
                    DisplayPowerStatusEnum.UNPLUGGED,
                ]

                main()
                mock_toggle_display_power_status.assert_not_called()


def test_power_on_display_with_attempting_はディスプレイの消費電力が異常な値を示している_TROUBLE_の場合_内部からtoggle_display_power_statusメソッドが一度も呼ばれないこと():
    # get_wattages_on_display をモック化して
    # 数秒間の測定なしに、即時に固定のワット数を返すようにして、テストを高速化
    with patch(
            'raspberry_pi_media_controller.power_on_display_with_attempting.get_wattages_on_display'
    ) as mock_get_wattages_on_display:
        mock_get_wattages_on_display.return_value = [30, 30, 30, 30]

        # toggle_display_power_status をモック化して
        # 呼び出し回数をアサート
        with patch(
                'raspberry_pi_media_controller.power_on_display_with_attempting.toggle_display_power_status'
        ) as mock_toggle_display_power_status:
            # get_display_power_status をモック化して、
            # 呼び出し毎にテストの意図に合う値を返す
            with patch(
                    'raspberry_pi_media_controller.power_on_display_with_attempting.get_display_power_status'
            ) as mock_get_display_power_status:
                mock_get_display_power_status.side_effect = [
                    DisplayPowerStatusEnum.TROUBLE,
                ]

                main()
                mock_toggle_display_power_status.assert_not_called()
