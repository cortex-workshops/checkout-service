import pytest

from checkout.cart import apply_promo, can_checkout, subtotal


def test_subtotal():
    assert subtotal([{"price": 10.0, "qty": 2}, {"price": 5.5, "qty": 1}]) == 25.5


def test_apply_promo():
    assert apply_promo(100, "VIP20") == 80


def test_bad_promo():
    with pytest.raises(ValueError):
        apply_promo(100, "NOPE")


def test_can_checkout():
    assert can_checkout([{"price": 1, "qty": 1}], True)
    assert not can_checkout([], True)
