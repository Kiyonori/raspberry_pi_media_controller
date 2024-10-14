from raspberry_pi_media_controller.data.display_power_config_data import DisplayPowerConfigData
from raspberry_pi_media_controller.enums.display_power_status_enums import DisplayPowerStatusEnum
from raspberry_pi_media_controller.modules.config.get_display_power_config import get_display_power_config


def get_last_message_on_power_on_display(
        attempt_count: int,
        power_status: DisplayPowerStatusEnum,
) -> str:
    """
    ディスプレイ電源ON時の最終状態をメッセージとして取得する

    :param attempt_count: 試行回数
    :type attempt_count: int
    :param power_status: ディスプレイの電源状態
    :type power_status: DisplayPowerStatusEnum
    :return: ディスプレイ電源ON時の最終状態
    :rtype: str
    """

    config: DisplayPowerConfigData = get_display_power_config()

    if power_status is DisplayPowerStatusEnum.UNPLUGGED:
        return 'The display power plug is unplugged.'

    if power_status is DisplayPowerStatusEnum.TROUBLE:
        return 'The display power consumption is excessive.'

    if attempt_count == 0:
        if power_status is DisplayPowerStatusEnum.POWERED_ON:
            return 'The display is already powered on.'

    elif attempt_count <= config.handling_maximum_number_of_attempts:
        return 'The display is powered on now.'

    return 'The system could not turn on the display.'
