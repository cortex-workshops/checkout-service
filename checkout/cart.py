def subtotal(items):
    return round(sum(i["price"] * i["qty"] for i in items), 2)


def apply_promo(total, code):
    promos = {"SPRING10": 0.10, "VIP20": 0.20}
    if code not in promos:
        raise ValueError(f"Unknown promo code: {code}")
    return round(total * (1 - promos[code]), 2)


def can_checkout(items, has_payment_method):
    return bool(items) and has_payment_method
