import os
from raspberry_pi_media_controller.modules.my_load_dotenv import my_load_dotenv
import subprocess


def toggle_display_power_status() -> None:
    """
    ディスプレイの電源を操作するための信号を送信する
    このメソッドは、ディスプレイの電源の状態は考慮しません
    ただ、送信するだけのメソッドです
    """

    my_load_dotenv()

    external_executable: str = os.environ.get('EXTERNAL_SCRIPT_PREFIX')
    gpio: str = os.environ.get('DISPLAY_CONTROL_INFRARED_LED_GPIO_PORT')
    json_and_key: str = os.environ.get('DISPLAY_POWER_SIGNAL_JSON')

    external_command: str = (
            '%s -p -g%s -f %s' %
            (external_executable, gpio, json_and_key)
    )

    subprocess.run(external_command.split(' '))
