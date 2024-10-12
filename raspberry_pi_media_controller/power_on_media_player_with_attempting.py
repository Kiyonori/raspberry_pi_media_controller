from raspberry_pi_media_controller.data.media_player_power_config_data \
    import MediaPlayerPowerConfigData
from raspberry_pi_media_controller.enums.media_player_power_status_enum \
    import MediaPlayerPowerStatusEnum
from raspberry_pi_media_controller.modules.analog_digital_converter.get_wattages_on_media_player \
    import get_wattages_on_media_player
from raspberry_pi_media_controller.modules.config.get_media_player_power_config \
    import get_media_player_power_config
from raspberry_pi_media_controller.modules.get_power_statuses.get_media_player_power_status \
    import get_media_player_power_status
from raspberry_pi_media_controller.modules.send_infrared_signals.toggle_media_player_power_status \
    import toggle_media_player_power_status
from time import sleep


def main():
    """
    メディアプレイヤーの電源を最大N回の試行で付ける
    """
    attempt_count: int = 0
    config: MediaPlayerPowerConfigData = get_media_player_power_config()
    power_status: MediaPlayerPowerStatusEnum

    while True:
        wattages: list[float] = get_wattages_on_media_player()
        power_status = get_media_player_power_status(wattages)

        if power_status in {
            MediaPlayerPowerStatusEnum.POWERED_ON,
            MediaPlayerPowerStatusEnum.UNPLUGGED,
            MediaPlayerPowerStatusEnum.TROUBLE,
        }:
            break

        if attempt_count > config.handling_maximum_number_of_attempts - 1:
            break

        toggle_media_player_power_status()
        sleep(config.handling_waiting_seconds)
        attempt_count += 1


if __name__ == "__main__":
    main()
