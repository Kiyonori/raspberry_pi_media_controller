from raspberry_pi_media_controller.data.media_player_power_config_data import MediaPlayerPowerConfigData
from raspberry_pi_media_controller.enums.media_player_power_status_enum import MediaPlayerPowerStatusEnum
from raspberry_pi_media_controller.modules.config.get_media_player_power_config import get_media_player_power_config


def get_last_message_on_power_on_media_player(
        attempt_count: int,
        power_status: MediaPlayerPowerStatusEnum,
) -> str:
    """
    メディアプレイヤー電源ON時の最終状態をメッセージとして取得する

    :param attempt_count: 試行回数
    :type attempt_count: int
    :param power_status: メディアプレイヤーの電源状態
    :type power_status: MediaPlayerPowerStatusEnum
    :return: メディアプレイヤー電源ON時の最終状態
    :rtype: str
    """

    config: MediaPlayerPowerConfigData = get_media_player_power_config()

    if power_status is MediaPlayerPowerStatusEnum.UNPLUGGED:
        return 'The media player power plug is unplugged.'

    if power_status is MediaPlayerPowerStatusEnum.TROUBLE:
        return 'The media player power consumption is excessive.'

    if attempt_count == 0:
        if power_status is MediaPlayerPowerStatusEnum.POWERED_ON:
            return 'The media player is already powered on.'

    elif attempt_count <= config.handling_maximum_number_of_attempts:
        return 'The media player is powered on now.'

    return 'The system could not turn on the media player.'
