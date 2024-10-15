import logging

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
from raspberry_pi_media_controller.modules.my_logger.flatten_wattages \
    import flatten_wattages
from raspberry_pi_media_controller.modules.my_logger.get_last_message_on_power_on_display \
    import get_last_message_on_power_on_display
from raspberry_pi_media_controller.modules.my_logger.initialize_logger \
    import initialize_logger
from raspberry_pi_media_controller.modules.my_logger.make_log_directory \
    import make_log_directory
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
    log_dir: str = make_log_directory()
    initialize_logger(log_dir)
    logging.info('The system will turn on the display.')

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

        logging.info(
            'Attempt %d times: Turn on the power to the display. Wattages: %s' %
            (
                int(attempt_count + 1),
                flatten_wattages(wattages),
            )
        )

        toggle_display_power_status()
        sleep(config.handling_waiting_seconds)
        attempt_count += 1

    last_message: str = get_last_message_on_power_on_display(
        attempt_count,
        power_status,
    )

    logging.info(
        last_message + \
        ' Wattages: ' + \
        flatten_wattages(wattages)
    )


if __name__ == "__main__":
    main()
