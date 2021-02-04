from django.core.exceptions import ValidationError


def validate_pump(pump_num):
    if pump_num <= 9:
        raise ValidationError(
            f"{pump_num} is not a valid pump",
            params={'pump_num': pump_num }
    )