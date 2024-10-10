from raspberry_pi_media_controller.enums.media_player_power_status_enum \
    import MediaPlayerPowerStatusEnum
from raspberry_pi_media_controller.modules.analog_digital_converter.get_wattages_on_media_player \
    import get_wattages_on_media_player
from raspberry_pi_media_controller.modules.get_power_statuses.get_media_player_power_status \
    import get_media_player_power_status
from raspberry_pi_media_controller.modules.send_infrared_signals.toggle_media_player_power_status \
    import toggle_media_player_power_status


def power_off_media_player() -> None:
    """
    メディアプレイヤーの消費電力を測定し、メディアプレイヤーが稼働している場合、
    終了を意味する赤外線信号を送信し、メディアプレイヤーを終了させる。

    ただし再試行は行いません。
    """

    wattages: list[float] = get_wattages_on_media_player()
    power_status: MediaPlayerPowerStatusEnum = get_media_player_power_status(
        wattages
    )

    if power_status is not MediaPlayerPowerStatusEnum.POWERED_ON:
        return

    toggle_media_player_power_status()
