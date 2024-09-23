from raspberry-pi-media-controller.modules.my_sum import my_sum


def test_my_sum() -> None:
    result = my_sum(1.0, 2.0)
    assert result == 3.0