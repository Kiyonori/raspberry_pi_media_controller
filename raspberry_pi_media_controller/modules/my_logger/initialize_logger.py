from datetime import datetime
import logging
import os


def initialize_logger(log_dir: str) -> None:
    """
    ログの出力先Pathやファイル名を初期設定する
    :param log_dir: ログの出力先Path
    :type log_dir: str
    """

    file_name: str = datetime.now().strftime("%Y%m%d.log")

    file_path: str = os.path.join(
        log_dir,
        file_name,
    )

    logging.basicConfig(
        filename=file_path,
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
