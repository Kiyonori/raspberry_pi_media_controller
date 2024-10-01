from raspberry_pi_media_controller.enums.display_power_status_enums \
    import DisplayPowerStatusEnum


def get_display_power_status(wattages: list[float]) -> DisplayPowerStatusEnum:
    """
    消費電力からディスプレイの電源状態を判別する
    :param wattages: 複数回測定した消費電力
    :type wattages: list[float]
    :return: ディスプレイの電源状態を示すEnum
    """

    previous_status: DisplayPowerStatusEnum | None = None
    current_status: DisplayPowerStatusEnum = DisplayPowerStatusEnum.GLITCHED

    for wattage in wattages:
        if wattage <= 0.4:
            current_status = DisplayPowerStatusEnum.UNPLUGGED

        elif wattage >= 2.4 and wattage <= 3.0:
            current_status = DisplayPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_NOT_BE_RECEIVED

        elif wattage >= 17.0 and wattage <= 20.0:
            current_status = DisplayPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED

        elif wattage >= 55.0 and wattage <= 160.0:
            current_status = DisplayPowerStatusEnum.POWERED_ON

        elif wattage > 160.0:
            return DisplayPowerStatusEnum.TROUBLE

        else:
            return DisplayPowerStatusEnum.GLITCHED

        if previous_status is None:
            previous_status = current_status
            continue

        if current_status != previous_status:
            return DisplayPowerStatusEnum.GLITCHED

    return current_status
