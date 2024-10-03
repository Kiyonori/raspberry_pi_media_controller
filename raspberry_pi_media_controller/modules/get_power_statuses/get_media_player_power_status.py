from raspberry_pi_media_controller.data.media_player_power_config_data \
    import MediaPlayerPowerConfigData
from raspberry_pi_media_controller.enums.media_player_power_status_enum \
    import MediaPlayerPowerStatusEnum
from raspberry_pi_media_controller.modules.config.get_media_player_power_config \
    import get_media_player_power_config


def get_media_player_power_status(wattages: list[float]) -> MediaPlayerPowerStatusEnum:
    """
    消費電力からメディアプレイヤーの電源状態を判別する
    :param wattages: 複数回測定した消費電力
    :type wattages: list[float]
    :return: メディアプレイヤーの電源状態を示すEnum
    """

    previous_status: MediaPlayerPowerStatusEnum | None = None
    current_status: MediaPlayerPowerStatusEnum = MediaPlayerPowerStatusEnum.GLITCHED
    power_config: MediaPlayerPowerConfigData = get_media_player_power_config()

    for wattage in wattages:
        if wattage <= power_config.unplugged_wattage:
            current_status = MediaPlayerPowerStatusEnum.UNPLUGGED

        elif wattage >= power_config.powered_off_and_signal_can_be_received_wattages[0] \
                and wattage <= power_config.powered_off_and_signal_can_be_received_wattages[1]:
            current_status = MediaPlayerPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED

        elif wattage >= power_config.powered_on_wattages[0] \
                and wattage <= power_config.powered_on_wattages[1]:
            current_status = MediaPlayerPowerStatusEnum.POWERED_ON

        elif wattage >= power_config.trouble_wattage:
            return MediaPlayerPowerStatusEnum.TROUBLE

        else:
            return MediaPlayerPowerStatusEnum.GLITCHED

        if previous_status is None:
            previous_status = current_status
            continue

        if current_status != previous_status:
            return MediaPlayerPowerStatusEnum.GLITCHED

    return current_status
