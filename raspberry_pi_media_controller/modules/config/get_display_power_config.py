import os
from dotenv import load_dotenv
from raspberry_pi_media_controller.data.display_power_config_data \
    import DisplayPowerConfigData


def get_display_power_config() -> DisplayPowerConfigData:
    """
    ディスプレイの消費電力に関する設定値を参照する
    """

    load_dotenv()

    unplugged_wattage = float(
        os
        .environ
        .get('DISPLAY_POWER_SUPPLY_STATUS_UNPLUGGED')
    )

    powered_off_and_signal_can_not_be_received_wattages = [
        float(
            os
            .environ
            .get('DISPLAY_POWER_SUPPLY_STATUS_SIGNAL_CAN_NOT_BE_RECEIVED')
            .split(',')[0]
        ),
        float(
            os
            .environ
            .get('DISPLAY_POWER_SUPPLY_STATUS_SIGNAL_CAN_NOT_BE_RECEIVED')
            .split(',')[1]
        ),
    ]

    powered_off_and_signal_can_be_received_wattages = [
        float(
            os
            .environ
            .get('DISPLAY_POWER_SUPPLY_STATUS_SIGNAL_CAN_BE_RECEIVED')
            .split(',')[0]
        ),
        float(
            os
            .environ
            .get('DISPLAY_POWER_SUPPLY_STATUS_SIGNAL_CAN_BE_RECEIVED')
            .split(',')[1]
        ),
    ]

    powered_on_wattages = [
        float(
            os
            .environ
            .get('DISPLAY_POWER_SUPPLY_STATUS_POWERED_ON')
            .split(',')[0]
        ),
        float(
            os
            .environ
            .get('DISPLAY_POWER_SUPPLY_STATUS_POWERED_ON')
            .split(',')[1]
        ),
    ]

    trouble_wattage = float(
        os
        .environ
        .get('DISPLAY_POWER_SUPPLY_STATUS_TROUBLE')
    )

    return DisplayPowerConfigData(
        unplugged_wattage,
        powered_off_and_signal_can_not_be_received_wattages,
        powered_off_and_signal_can_be_received_wattages,
        powered_on_wattages,
        trouble_wattage,
    )
