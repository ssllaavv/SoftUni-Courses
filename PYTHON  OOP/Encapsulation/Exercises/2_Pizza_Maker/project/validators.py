
def validate_topping_type(value):
    if value == "":
        raise ValueError("The topping type cannot be an empty string")


def validate_gte_zero(value):
    if value <= 0:
        raise ValueError("The weight cannot be less or equal to zero")