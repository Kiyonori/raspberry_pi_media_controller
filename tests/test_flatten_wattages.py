import pytest

from raspberry_pi_media_controller.modules.my_logger.flatten_wattages import flatten_wattages


@pytest.mark.parametrize(
    "input_wattages, expected_wattages",
    [
        (
                [12.345, 23.456789, 34.5678, 45.678901],
                '12.34, 23.45, 34.56, 45.67'
        ),
    ],
)
def test_flatten_wattages_メソッドは意図した変換をおこなっていること(
        input_wattages: list[float],
        expected_wattages: str,
):
    result: str = flatten_wattages(
        input_wattages,
        number_of_digits=2
    )

    assert type(result) == str
    assert result == expected_wattages
