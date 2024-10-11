from raspberry_pi_media_controller.data.display_power_config_data \
    import DisplayPowerConfigData
from raspberry_pi_media_controller.enums.display_power_status_enums \
    import DisplayPowerStatusEnum
from raspberry_pi_media_controller.modules.analog_digital_converter.get_wattages_on_display \
    import get_wattages_on_display
from raspberry_pi_media_controller.modules.config.get_display_power_config \
    import get_display_power_config
from raspberry_pi_media_controller.modules.get_power_statuses.get_display_power_status \
    import get_display_power_status
from raspberry_pi_media_controller.modules.send_infrared_signals.toggle_display_power_status \
    import toggle_display_power_status
from time import sleep


def main():
    """
    ディスプレイの電源を最大N回の試行で付ける
    """

    attempt_count: int = 0
    config: DisplayPowerConfigData = get_display_power_config()
    power_status: DisplayPowerStatusEnum

    while True:
        wattages: list[float] = get_wattages_on_display()
        power_status = get_display_power_status(wattages)

        if power_status in {
            DisplayPowerStatusEnum.POWERED_ON,
            DisplayPowerStatusEnum.UNPLUGGED,
            DisplayPowerStatusEnum.TROUBLE,
        }:
            break

        if attempt_count > config.handling_maximum_number_of_attempts - 1:
            break

        toggle_display_power_status()
        sleep(config.handling_waiting_seconds)
        attempt_count += 1


if __name__ == "__main__":
    main()
