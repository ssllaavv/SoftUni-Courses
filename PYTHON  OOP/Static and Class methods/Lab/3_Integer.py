from math import floor


class Integer:

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            value = floor(float_value)
            return cls(value)
        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        for char in value:
            num = roman_numerals[char]
            if num > prev_value:
                total += num - 2 * prev_value
            else:
                total += num
            prev_value = num
        return cls(total)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            value = int(value)
            return cls(value)
        return "wrong type"


# first_num = Integer(10)
# print(first_num.value)
#
# second_num = Integer.from_roman("IV")
# print(second_num.value)
#
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))


