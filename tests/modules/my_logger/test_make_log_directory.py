from datetime import datetime
import os
from raspberry_pi_media_controller.modules.my_logger.make_log_directory import make_log_directory
import shutil


def test_make_log_directory_メソッドは_年月のディレクトリを作成すること():
    now: datetime = datetime.now()

    directory: str = os.path.join(
        'logs',
        'testing',
        now.strftime('%Y'),
        now.strftime('%Y%m'),
    )

    # テスト実行前にディレクトリを削除する
    shutil.rmtree(directory, ignore_errors=True)

    # テスト実行前には、ディレクトリが存在しないことを確認する
    assert False == os.path.isdir(directory)

    # テスト対象のメソッドを呼ぶ
    make_log_directory()

    # テスト対象のメソッドを実行後に、ディレクトリが存在することを確認する
    assert os.path.isdir(directory)


def test_make_log_directory_メソッドは_年_年月のPath文字列を返してくること():
    now: datetime = datetime.now()

    directory: str = os.path.join(
        'logs',
        'testing',
        now.strftime('%Y'),
        now.strftime('%Y%m'),
    )

    made_directory: str = make_log_directory()

    assert made_directory == directory
