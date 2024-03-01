import pytest

from converter import roman_to_decimal


@pytest.mark.parametrize(
    "value,expected",
    [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ],
)
def test_valid_roman_numerals(value, expected):
    assert roman_to_decimal(value) == expected


def test_lower_case_input():
    assert roman_to_decimal("ix") == 9


@pytest.mark.parametrize("invalid", ["IIII", "VV", "XXXX", "LC", "DM"])
def test_invalid_roman_numerals(invalid):
    with pytest.raises(ValueError):
        roman_to_decimal(invalid)


def test_empty_string():
    with pytest.raises(ValueError):
        roman_to_decimal("")


@pytest.mark.parametrize("non_string", [123, None, 5.5, [], {}])
def test_non_string_input(non_string):
    with pytest.raises(ValueError):
        roman_to_decimal(non_string)


def test_spaces_around_numerals():
    assert roman_to_decimal(" IX ") == 9


@pytest.mark.parametrize(
    "value,expected",
    [
        ("mcmxcix", 1999),
        ("cdxliv", 444),
    ],
)
def test_complex_valid_cases_lowercase(value, expected):
    assert roman_to_decimal(value) == expected


@pytest.mark.parametrize("value", ["A", "23", "Roman"])
def test_invalid_characters(value):
    with pytest.raises(ValueError):
        roman_to_decimal(value)


@pytest.mark.parametrize("invalid", ["OII", "IL", "IC", "IIV", "XXC"])
def test_invalid_combinations_and_subtractions(invalid):
    with pytest.raises(ValueError):
        roman_to_decimal(invalid)


def test_multiple_valid_subtraction_scenarios():
    assert roman_to_decimal("XIX") == 19  # Test for "19" with two subtractions


@pytest.mark.parametrize(
    "large_numeral,expected",
    [
        ("MMMMCMXCIX", 4999),
    ],
)
def test_extremely_large_numbers(large_numeral, expected):
    assert roman_to_decimal(large_numeral) == expected


@pytest.mark.parametrize(
    "uncommon_but_valid,expected",
    [
        ("VL", 45),  # Though uncommon, some might use it
    ],
)
def test_uncommon_valid_numerals(uncommon_but_valid, expected):
    assert roman_to_decimal(uncommon_but_valid) == 45


def test_whitespace_within_numerals():
    with pytest.raises(ValueError):
        roman_to_decimal("I X")


def test_consecutive_valid_subtraction_pairs():
    assert roman_to_decimal("IXIX") == 18


def test_decremental_sequences_across_subtraction_boundaries():
    assert roman_to_decimal("XIV") == 14


@pytest.mark.parametrize("invalid", ["IIIIX", "IIX"])
def test_invalid_subtractive_repetitions(invalid):
    with pytest.raises(ValueError):
        roman_to_decimal(invalid)


def test_mixed_case_input():
    assert roman_to_decimal("mCmXcIv") == 1994


@pytest.mark.parametrize(
    "non_standard,expected",
    [
        ("IC", 99),
    ],
)
def test_non_standard_but_sometimes_seen_numerals(non_standard, expected):
    with pytest.raises(ValueError):
        roman_to_decimal(non_standard)


def test_edge_case_near_maximum_value():
    assert roman_to_decimal("MMMMCMXCVIII") == 4998


def test_invalid_sequences_mimicking_valid_patterns():
    with pytest.raises(ValueError):
        roman_to_decimal("IIX")


@pytest.mark.parametrize("value", ["VV", "LL", "DD", "CCCC"])
def test_error_messages_for_invalid_repetitions(value):
    with pytest.raises(ValueError) as exc_info:
        roman_to_decimal(value)
    assert "incorrect repetition" in str(exc_info.value)
