import os
from raspberry_pi_media_controller.data.media_player_power_config_data \
    import MediaPlayerPowerConfigData
from raspberry_pi_media_controller.modules.my_load_dotenv \
    import my_load_dotenv


def get_media_player_power_config():
    """
    メディアプレイヤーの消費電力に関する設定値を参照する
    """

    my_load_dotenv()

    unplugged_wattage = float(
        os
        .environ
        .get('MEDIA_PLAYER_POWER_SUPPLY_STATUS_UNPLUGGED')
    )

    powered_off_and_signal_can_be_received_wattages = [
        float(
            os
            .environ
            .get('MEDIA_PLAYER_POWER_SUPPLY_STATUS_SIGNAL_CAN_BE_RECEIVED')
            .split(',')[0]
        ),
        float(
            os
            .environ
            .get('MEDIA_PLAYER_POWER_SUPPLY_STATUS_SIGNAL_CAN_BE_RECEIVED')
            .split(',')[1]
        ),
    ]

    powered_on_wattages = [
        float(
            os
            .environ
            .get('MEDIA_PLAYER_POWER_SUPPLY_STATUS_POWERED_ON')
            .split(',')[0]
        ),
        float(
            os
            .environ
            .get('MEDIA_PLAYER_POWER_SUPPLY_STATUS_POWERED_ON')
            .split(',')[1]
        ),
    ]

    trouble_wattage = float(
        os
        .environ
        .get('MEDIA_PLAYER_POWER_SUPPLY_STATUS_TROUBLE')
    )

    handling_maximum_number_of_attempts = int(
        os
        .environ
        .get('MEDIA_PLAYER_HANDLING_MAXIMUM_NUMBER_OF_ATTEMPTS')
    )

    handling_waiting_seconds = int(
        os
        .environ
        .get('MEDIA_PLAYER_HANDLING_WAITING_SECONDS')
    )

    return MediaPlayerPowerConfigData(
        unplugged_wattage,
        powered_off_and_signal_can_be_received_wattages,
        powered_on_wattages,
        trouble_wattage,
        handling_maximum_number_of_attempts,
        handling_waiting_seconds,
    )
