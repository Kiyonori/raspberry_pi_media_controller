import os
from raspberry_pi_media_controller.modules.my_load_dotenv import my_load_dotenv
import subprocess


def toggle_media_player_power_status() -> None:
    """
    メディアプレイヤーの電源を操作するための信号を送信する
    このメソッドは、メディアプレイヤーの電源の状態は考慮しません
    ただ、送信するだけのメソッドです
    """

    my_load_dotenv()

    external_executable: str = os.environ.get('EXTERNAL_SCRIPT_PREFIX')
    gpio: str = os.environ.get('MEDIA_PLAYER_CONTROL_INFRARED_LED_GPIO_PORT')
    json_and_key: str = os.environ.get('MEDIA_PLAYER_POWER_SIGNAL_JSON')

    external_command: str = (
            '%s -p -g%s -f %s' %
            (external_executable, gpio, json_and_key)
    )

    subprocess.run(external_command.split(' '))
