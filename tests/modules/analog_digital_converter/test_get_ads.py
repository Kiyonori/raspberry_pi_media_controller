import pytest
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.ads1x15 import Mode
from raspberry_pi_media_controller.modules.analog_digital_converter.get_ads import get_ads


def test_get_ads_メソッドは_ADS1115インスタンスを返すこと():
    instance = get_ads()

    assert isinstance(
        instance,
        ADS1115,
    )


def test_get_ads_メソッドによってつくられたインスタンスのmodeは未指定の場合_CONTINUOUSであること():
    instance = get_ads()

    assert instance.mode is Mode.CONTINUOUS


def test_get_ads_メソッドによってつくられたインスタンスのdata_rateは_未指定の場合_860であること():
    instance = get_ads()

    assert instance.data_rate is 860


def test_get_ads_メソッドは_ADS1115インスタンスを返すこと():
    instance = get_ads()

    assert isinstance(
        instance,
        ADS1115,
    )


def test_get_ads_メソッドによってつくられたインスタンスのmodeは未指定の場合_CONTINUOUSであること():
    instance = get_ads()

    assert type(instance.mode) == int
    assert instance.mode == Mode.CONTINUOUS


def test_get_ads_メソッドによってつくられたインスタンスのdata_rateは_未指定の場合_860であること():
    instance = get_ads()

    assert type(instance.data_rate) == int
    assert instance.data_rate == 860


def test_get_ads_メソッドにconversion_modeを指定すると_そのとおりのインスタンスが作られること():
    instance = get_ads(
        conversion_mode=Mode.SINGLE,
    )

    assert type(instance.mode) == int
    assert instance.mode == Mode.SINGLE


@pytest.mark.parametrize(
    "data_rate, expected",
    [
        (8, 8),
        (16, 16),
        (32, 32),
        (64, 64),
        (128, 128),
        (250, 250),
        (475, 475),
        (860, 860),
    ],
)
def test_get_ads_メソッドにdata_rateを指定すると_そのとおりのインスタンスが作られること(
        data_rate,
        expected,
):
    instance = get_ads(
        samples_per_second=data_rate,
    )

    assert type(instance.data_rate) == int
    assert instance.data_rate == expected
