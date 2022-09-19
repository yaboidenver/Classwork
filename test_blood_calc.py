import pytest

@pytest.mark.parametrize('input_one, expected',
    [(85,"Normal"),
    (45,"Borderline low"),
    (35,"Low")])
def test_check_HDL_norm(input_one, expected):
    from blood_calc import check_HDL
    answer = check_HDL(input_one)
    assert answer == expected

"""
def test_check_HDL_borderline():
    from blood_calc import check_HDL
    answer = check_HDL(45)
    expected = "Borderline low"
    assert answer == expected

def test_check_HDL_low():
    from blood_calc import check_HDL
    answer = check_HDL(35)
    expected = "Low"
    assert answer == expected
"""