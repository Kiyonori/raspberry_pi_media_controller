from datetime import datetime
import os
import sys


def make_log_directory() -> str:
    """
    ログファイルを保持するためのディレクトリを作成する。
    実行時点の「年/年月」がディレクトリ名になります。
    :return 作成したディレクトリ名
    :rtype str
    """

    environment: str

    if "pytest" in sys.modules:
        environment = "testing"
    else:
        environment = "production"

    now = datetime.now()

    directory: str = os.path.join(
        'logs',
        environment,
        now.strftime('%Y'),
        now.strftime('%Y%m'),
    )

    os.makedirs(
        name=directory,
        exist_ok=True,
    )

    return directory
