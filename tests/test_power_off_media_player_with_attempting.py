from raspberry_pi_media_controller.enums.media_player_power_status_enum import MediaPlayerPowerStatusEnum
from raspberry_pi_media_controller.power_off_media_player_with_attempting import main
from unittest.mock import patch


def test_power_off_media_player_with_attempting_はメディアプレイヤーの電源状態が_POWERED_ON_であるとき_内部からtoggle_media_player_power_statusメソッドを呼び_メディアプレイヤーの終了を試みること():
    with patch(
            'raspberry_pi_media_controller.power_off_media_player_with_attempting.get_wattages_on_media_player'
    ) as mock_get_wattages_on_media_player:
        mock_get_wattages_on_media_player.return_value = [30, 30, 30, 30]

        # toggle_media_player_power_status をモック化して
        # 呼び出し回数をアサート
        with patch(
                'raspberry_pi_media_controller.power_off_media_player_with_attempting.toggle_media_player_power_status'
        ) as mock_toggle_media_player_power_status:
            # get_media_player_power_status をモック化して、
            # 呼び出し毎にテストの意図に合う値を返す
            with patch(
                    'raspberry_pi_media_controller.power_off_media_player_with_attempting.get_media_player_power_status'
            ) as mock_get_media_player_power_status:
                mock_get_media_player_power_status.side_effect = [
                    MediaPlayerPowerStatusEnum.POWERED_ON,  # ℹ️ 1回目
                    MediaPlayerPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED,  # ℹ️ 2回目
                ]

                main()
                mock_toggle_media_player_power_status.assert_called_once()


def test_power_off_media_player_with_attempting_はメディアプレイヤーの電源状態が_すでに_POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED_であるとき_内部からtoggle_media_player_power_statusメソッドが一度も呼ばれないこと():
    # get_wattages_on_media_player をモック化して
    # 数秒間の測定なしに、即時に固定のワット数を返すようにして、テストを高速化
    with patch(
            'raspberry_pi_media_controller.power_off_media_player_with_attempting.get_wattages_on_media_player'
    ) as mock_get_wattages_on_media_player:
        mock_get_wattages_on_media_player.return_value = [30, 30, 30, 30]

        # toggle_media_player_power_status をモック化して
        # 呼び出し回数をアサート
        with patch(
                'raspberry_pi_media_controller.power_off_media_player_with_attempting.toggle_media_player_power_status'
        ) as mock_toggle_media_player_power_status:
            # get_media_player_power_status をモック化して、
            # 呼び出し毎にテストの意図に合う値を返す
            with patch(
                    'raspberry_pi_media_controller.power_off_media_player_with_attempting.get_media_player_power_status'
            ) as mock_get_media_player_power_status:
                mock_get_media_player_power_status.side_effect = [
                    MediaPlayerPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED,  # ℹ️
                ]

                main()
                mock_toggle_media_player_power_status.assert_not_called()


def test_power_off_media_player_with_attempting_はメディアプレイヤーに電源が接続されていない_UNPLUGGED_の場合_内部からtoggle_media_player_power_statusメソッドが一度も呼ばれないこと():
    # get_wattages_on_media_player をモック化して
    # 数秒間の測定なしに、即時に固定のワット数を返すようにして、テストを高速化
    with patch(
            'raspberry_pi_media_controller.power_off_media_player_with_attempting.get_wattages_on_media_player'
    ) as mock_get_wattages_on_media_player:
        mock_get_wattages_on_media_player.return_value = [30, 30, 30, 30]

        # toggle_media_player_power_status をモック化して
        # 呼び出し回数をアサート
        with patch(
                'raspberry_pi_media_controller.power_off_media_player_with_attempting.toggle_media_player_power_status'
        ) as mock_toggle_media_player_power_status:
            # get_media_player_power_status をモック化して、
            # 呼び出し毎にテストの意図に合う値を返す
            with patch(
                    'raspberry_pi_media_controller.power_off_media_player_with_attempting.get_media_player_power_status'
            ) as mock_get_media_player_power_status:
                mock_get_media_player_power_status.side_effect = [
                    MediaPlayerPowerStatusEnum.UNPLUGGED,  # ℹ️
                ]

                main()
                mock_toggle_media_player_power_status.assert_not_called()


def test_power_off_media_player_with_attempting_はメディアプレイヤーの消費電力が異常な値を示している_TROUBLE_の場合_内部からtoggle_media_player_power_statusメソッドが一度も呼ばれないこと():
    # get_wattages_on_media_player をモック化して
    # 数秒間の測定なしに、即時に固定のワット数を返すようにして、テストを高速化
    with patch(
            'raspberry_pi_media_controller.power_off_media_player_with_attempting.get_wattages_on_media_player'
    ) as mock_get_wattages_on_media_player:
        mock_get_wattages_on_media_player.return_value = [30, 30, 30, 30]

        # toggle_media_player_power_status をモック化して
        # 呼び出し回数をアサート
        with patch(
                'raspberry_pi_media_controller.power_off_media_player_with_attempting.toggle_media_player_power_status'
        ) as mock_toggle_media_player_power_status:
            # get_media_player_power_status をモック化して、
            # 呼び出し毎にテストの意図に合う値を返す
            with patch(
                    'raspberry_pi_media_controller.power_off_media_player_with_attempting.get_media_player_power_status'
            ) as mock_get_media_player_power_status:
                mock_get_media_player_power_status.side_effect = [
                    MediaPlayerPowerStatusEnum.TROUBLE,  # ℹ️
                ]

                main()
                mock_toggle_media_player_power_status.assert_not_called()


def test_power_off_media_player_with_attempting_はメディアプレイヤーの電源状態が_POWERED_ON_であり_内部からtoggle_media_player_power_statusメソッドを複数回呼び_状態がPOWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVEDになるまで終了を試みること():
    # get_wattages_on_media_player をモック化して
    # 数秒間の測定なしに、即時に固定のワット数を返すようにして、テストを高速化
    with patch(
            'raspberry_pi_media_controller.power_off_media_player_with_attempting.get_wattages_on_media_player'
    ) as mock_get_wattages_on_media_player:
        mock_get_wattages_on_media_player.return_value = [30, 30, 30, 30]

        # toggle_media_player_power_status をモック化して
        # 呼び出し回数をアサート
        with patch(
                'raspberry_pi_media_controller.power_off_media_player_with_attempting.toggle_media_player_power_status'
        ) as mock_toggle_media_player_power_status:
            # get_media_player_power_status をモック化して、
            # 呼び出し毎にテストの意図に合う値を返す
            with patch(
                    'raspberry_pi_media_controller.power_off_media_player_with_attempting.get_media_player_power_status'
            ) as mock_get_media_player_power_status:
                mock_get_media_player_power_status.side_effect = [
                    MediaPlayerPowerStatusEnum.POWERED_ON,  # ℹ️
                    MediaPlayerPowerStatusEnum.POWERED_ON,  # ℹ️
                    MediaPlayerPowerStatusEnum.POWERED_ON,  # ℹ️
                    MediaPlayerPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED,  # ℹ️
                ]
                main()
                assert mock_toggle_media_player_power_status.call_count == 3


def test_power_off_media_player_with_attempting_はメディアプレイヤーの電源状態が_POWERED_ON_である場合_内部からtoggle_media_player_power_statusメソッドを呼んで終了を試みる最大回数は10回であること():
    # get_wattages_on_media_player をモック化して
    # 数秒間の測定なしに、即時に固定のワット数を返すようにして、テストを高速化
    with patch(
            'raspberry_pi_media_controller.power_off_media_player_with_attempting.get_wattages_on_media_player'
    ) as mock_get_wattages_on_media_player:
        mock_get_wattages_on_media_player.return_value = [30, 30, 30, 30]

        # toggle_media_player_power_status をモック化して
        # 呼び出し回数をアサート
        with patch(
                'raspberry_pi_media_controller.power_off_media_player_with_attempting.toggle_media_player_power_status'
        ) as mock_toggle_media_player_power_status:
            # get_media_player_power_status をモック化して、
            # 呼び出し毎にテストの意図に合う値を返す
            with patch(
                    'raspberry_pi_media_controller.power_off_media_player_with_attempting.get_media_player_power_status'
            ) as mock_get_media_player_power_status:
                # ℹ️
                mock_get_media_player_power_status.return_value = MediaPlayerPowerStatusEnum.POWERED_ON

                main()
                assert mock_toggle_media_player_power_status.call_count == 10
