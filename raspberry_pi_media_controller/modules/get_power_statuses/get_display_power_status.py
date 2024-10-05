from raspberry_pi_media_controller.data.display_power_config_data \
    import DisplayPowerConfigData
from raspberry_pi_media_controller.enums.display_power_status_enums \
    import DisplayPowerStatusEnum
from raspberry_pi_media_controller.modules.config.get_display_power_config \
    import get_display_power_config


def get_display_power_status(wattages: list[float]) -> DisplayPowerStatusEnum:
    """
    消費電力からディスプレイの電源状態を判別する
    :param wattages: 複数回測定した消費電力
    :type wattages: list[float]
    :return: ディスプレイの電源状態を示すEnum
    """

    previous_status: DisplayPowerStatusEnum | None = None
    current_status: DisplayPowerStatusEnum = DisplayPowerStatusEnum.GLITCHED
    power_config: DisplayPowerConfigData = get_display_power_config()

    for wattage in wattages:
        if wattage <= power_config.unplugged_wattage:
            current_status = DisplayPowerStatusEnum.UNPLUGGED

        elif wattage >= power_config.powered_off_and_signal_can_be_received_wattages[0] \
                and wattage <= power_config.powered_off_and_signal_can_be_received_wattages[1]:
            current_status = DisplayPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED

        elif wattage >= power_config.powered_on_wattages[0] \
                and wattage <= power_config.powered_on_wattages[1]:
            current_status = DisplayPowerStatusEnum.POWERED_ON

        elif wattage >= power_config.trouble_wattage:
            return DisplayPowerStatusEnum.TROUBLE

        else:
            return DisplayPowerStatusEnum.GLITCHED

        if previous_status is None:
            previous_status = current_status
            continue

        if current_status != previous_status:
            return DisplayPowerStatusEnum.GLITCHED

    return current_status
