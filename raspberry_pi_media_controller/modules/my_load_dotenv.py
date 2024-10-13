from dotenv import load_dotenv
import os
import sys


def my_load_dotenv() -> None:
    """
    pytest として実行されている場合は .env.testing ファイルを読み込み、
    そうでない場合は .env ファイルを読み込む
    """
    if "pytest" in sys.modules:
        basename: str = os.path.basename(os.getcwd())
        load_dotenv(dotenv_path=basename + '/.env.testing')
        return

    load_dotenv()
