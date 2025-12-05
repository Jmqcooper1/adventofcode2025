import pytest
from conftest import import_day

main = import_day(3)
find_largest_two_digits = main.find_largest_two_digits
find_largest_twelve_digits = main.find_largest_x_digits

@pytest.fixture
def test_banks():
    """Fixture providing test bank data as plain text with \\n on each line."""
    return "987654321111111\n811111111111119\n234234234234278\n818181911112111\n"

def test_find_largest_two_digits(test_banks):
    """Test find_largest_two_digits function with fixture data."""
    banks : list[list[int]] = [
        list[int](map(int, list[str](line)))
        for line in test_banks.split('\n')
        if line.strip()  # only include non-empty lines
    ]
    results: list[int] = [find_largest_two_digits(bank) for bank in banks]
    print("test results are: ", results)
    
    assert results == [98, 89, 78, 92]
    assert sum(results) == 357

def test_find_largest_twelve_digits(test_banks):
    """Test find_largest_twelve_digits function with fixture data."""
    banks : list[list[int]] = [
        list[int](map(int, list[str](line)))
        for line in test_banks.split('\n')
        if line.strip()  # only include non-empty lines
    ]
    results: list[int] = [find_largest_twelve_digits(bank, 12) for bank in banks]
    print("test results are: ", results)
    
    assert results == [987654321111, 811111111119, 434234234278, 888911112111]
    assert sum(results) == 3121910778619



