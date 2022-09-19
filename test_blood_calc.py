import pytest

@pytest.mark.parametrize('HDL_input, expected',
    [(85,"Normal"),
    (45,"Borderline low"),
    (35,"Low")])
def test_check_HDL_norm(HDL_input, expected):
    from blood_calc import check_HDL
    answer = check_HDL(HDL_input)
    assert answer == expected


@pytest.mark.parametrize('LDL_input, expected',
    [(195, "Very High"),
    (165, "High"),
    (135, "Borderline High"),
    (120, "Normal")])
def test_check_LDL(LDL_input, expected):
    from blood_calc import check_LDL
    answer = check_LDL(LDL_input)
    assert answer == expected


@pytest.mark.parametrize('chol_input, expected',
    [(245, "High"),
    (235, "Borderline High"),
    (180, "Normal")])
def test_check_Chol(chol_input, expected):
    from blood_calc import check_Chol
    answer = check_Chol(chol_input)
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