ROMAN_NUMERALS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
VALID_PRECEDENCE = {"I": ("V", "X"), "X": ("L", "C"), "C": ("D", "M"), "V": ("L",)}
INVALID_REPETITIONS = ["VV", "LL", "DD", "IIII", "XXXX", "CCCC"]
INVALID_PAIRS = ["LC", "DM"]


def validate_roman_number(roman: str) -> None:
    if not roman:
        raise ValueError("Received empty roman number as an input.")

    if not all(char in ROMAN_NUMERALS for char in roman):
        raise ValueError("Invalid Roman numeral")

    for repetition in INVALID_REPETITIONS:
        if repetition in roman:
            raise ValueError(
                f"Invalid Roman numeral due to incorrect repetition: '{repetition}'."
            )

    for invalid_pair in INVALID_PAIRS:
        if invalid_pair in roman:
            raise ValueError(
                f"Invalid Roman numeral due to incorrect numeral pair: '{invalid_pair}'."
            )

    prev_char = None

    for i, char in enumerate(roman[:-1]):
        # Check for valid subtraction
        if char in VALID_PRECEDENCE and roman[i + 1] not in VALID_PRECEDENCE[char]:
            if ROMAN_NUMERALS[char] < ROMAN_NUMERALS[roman[i + 1]]:
                raise ValueError(
                    f"Invalid Roman numeral due to incorrect subtraction order: '{char}{roman[i+1]}'."
                )

        # Check for invalid subtraction using previous character
        if prev_char == char and ROMAN_NUMERALS[char] < ROMAN_NUMERALS[roman[i + 1]]:
            raise ValueError(
                f"Invalid Roman numeral due to incorrect use of subtraction: '{prev_char}{char}{roman[i+1]}'."
            )

        prev_char = char


def roman_to_decimal(roman: str) -> int:
    if not isinstance(roman, str):
        raise ValueError(
            f"Expected argument to be instance of 'str', instead got type {type(roman)}."
        )

    roman = roman.upper().strip()  # Convert all letters to uppercase and strip spaces

    validate_roman_number(roman)

    decimal = 0
    prev_value = 0

    for char in reversed(roman):
        value = ROMAN_NUMERALS[char]

        if value < prev_value:
            decimal -= value
        else:
            decimal += value

        prev_value = value

    return decimal
