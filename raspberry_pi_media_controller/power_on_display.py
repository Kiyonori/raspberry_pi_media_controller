from raspberry_pi_media_controller.enums.display_power_status_enums \
    import DisplayPowerStatusEnum
from raspberry_pi_media_controller.modules.analog_digital_converter.get_wattages_on_display \
    import get_wattages_on_display
from raspberry_pi_media_controller.modules.get_power_statuses.get_display_power_status \
    import get_display_power_status
from raspberry_pi_media_controller.modules.send_infrared_signals.toggle_display_power_status \
    import toggle_display_power_status


def power_on_display() -> None:
    """
    ディスプレイの消費電力を測定し、ディスプレイが稼働していない場合、
    電源投入のための赤外線信号を送信し、ディスプレイを稼働させる。

    ただし再試行は行いません。
    """

    wattages: list[float] = get_wattages_on_display()
    power_status: DisplayPowerStatusEnum = get_display_power_status(
        wattages
    )

    if power_status is not DisplayPowerStatusEnum.POWERED_OFF_AND_SIGNAL_CAN_BE_RECEIVED:
        return

    toggle_display_power_status()


power_on_display()
