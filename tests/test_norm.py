import pytest

from mypackage.norm import norm


def test_norm():
    assert norm(0, 0) == 0
    assert norm(0, 1) == 1
