from typing import Union

import pytest

from backend.formulas.basic_vitals import (get_homa_ir, get_bmi, get_blood_pressure, get_maximum_heart_rate,
                                           get_target_heart_rate, get_tg_hdl_ratio, get_triglyceride_glucose_index,
                                           get_atherogenic_index_of_plasma, get_body_adiposity_index,
                                           get_visceral_adiposity_index, get_lipid_accumulation_product,
                                           get_fatty_liver_index, get_waist_height_ratio, get_alt_ast_ratio, get_egfr,
                                           get_estimated_average_glucose, GENDER_ERROR_MESSAGE)


@pytest.mark.parametrize(
    'insulin, glucose, expected',
    [
        (41.9, 126, 13.04),
        (9.1, 96, 2.16),
        (8.1, 107, 2.14),
        (18.2, 168, 7.55)
    ]
)
def test_get_homa_ir(insulin: float, glucose: float, expected: float):
    """
    Test the get HOMA IR function.
    :param insulin: Insulin value of patient.
    :param glucose: Glucose value of patient.
    :param expected: Expected HOMA IR value.
    """
    assert get_homa_ir(insulin=insulin, glucose=glucose) == expected


@pytest.mark.parametrize(
    'weight, height, expected',
    [
        (95.7, 166, 34.7),
        (84.7, 166, 30.7),
        (82.6, 166, 30.0),
        (86.8, 166, 31.5),
    ]
)
def test_get_bmi(weight: float, height: float, expected: float):
    """
    Test the get BMI function.
    :param weight: Weight of patient.
    :param height: Height of patient.
    :param expected: Expected BMI.
    """
    assert get_bmi(weight=weight, height=height) == expected


@pytest.mark.parametrize(
    'systolic_bp, diastolic_bp, expected',
    [
        (147, 91, 'Grade 1'),
        (147, 86, 'Grade 1'),
        (150, 90, 'Grade 1'),
        (165, 97, 'Grade 2'),
    ]
)
def test_get_blood_pressure(systolic_bp: int, diastolic_bp: int, expected: str):
    """
    Test the get blood pressure function.
    :param systolic_bp: Systolic blood pressure.
    :param diastolic_bp: Diastolic blood pressure.
    :param expected: Expected blood pressure.
    """
    assert get_blood_pressure(systolic_bp=systolic_bp, diastolic_bp=diastolic_bp) == expected


@pytest.mark.parametrize(
    'age, expected',
    [
        (65, 155),
        (66, 154),
        (67, 153),
        (68, 152)
    ]
)
def test_get_maximum_heart_rate(age: int, expected: int):
    """
    Test the get maximum heart rate function.
    :param age: Age of patient.
    :param expected: Expected maximum heart rate.
    """
    assert get_maximum_heart_rate(age=age) == expected


@pytest.mark.parametrize(
    'maximum_heart_rate, expected',
    [
        (155, '77.5 - 131')
    ]
)
def test_get_target_heart_rate(maximum_heart_rate: int, expected: str):
    """
    Test the get target heart rate function.
    :param maximum_heart_rate: Maximum heart rate for patient.
    :param expected: Expected target heart rate.
    """
    assert get_target_heart_rate(maximum_heart_rate=maximum_heart_rate) == expected


@pytest.mark.parametrize(
    'tg, hdl, expected',
    [
        (142, 32, 4.44),
        (110, 32, 3.44),
        (129, 38, 3.39),
        (109, 35, 3.11),
    ]
)
def test_get_tg_hdl_ratio(tg: int, hdl: int, expected: float):
    """
    Test the get TG/HDL ratio.
    :param tg: Triglyceride value.
    :param hdl: HDL value.
    :param expected: Expected TG/HDL radio.
    """
    assert get_tg_hdl_ratio(tg, hdl) == expected


@pytest.mark.parametrize(
    'tg, glucose, expected',
    [
        (142, 126, 4.9),
        (110, 96, 4.63),
        (129, 107, 4.77),
        (109, 168, 4.91),
    ]
)
def test_get_triglyceride_glucose_index(tg: int, glucose: int, expected: float):
    """
    Test the get triglyceride glucose index function.
    :param tg: Triglyceride value.
    :param glucose: Glucose value.
    :param expected: Expected triglyceride glucose index.
    """
    assert get_triglyceride_glucose_index(tg=tg, glucose=glucose) == expected


@pytest.mark.parametrize(
    'tg, hdl, expected',
    [
        (142, 32, 0.29),
        (110, 32, 0.18),
        (129, 38, 0.17),
        (109, 35, 0.13)
    ]
)
def test_get_atherogenic_index_of_plasma(tg: int, hdl: int, expected: float):
    """
    Test the get atherogenic index of plasma function.
    :param tg: Triglyceride value.
    :param hdl: HDL value.
    :param expected: Expected atherogenic index of plasma value.
    """
    assert get_atherogenic_index_of_plasma(tg=tg, hdl=hdl) == expected


@pytest.mark.parametrize(
    'waist, height, expected',
    [
        (111, 166, 34),
        (101, 166, 29),
        (99, 166, 28),
        (101, 166, 29)
    ]
)
def test_get_body_adiposity_index(waist: int, height: int, expected: int):
    """
    Test the get body adiposity index function.
    :param waist: Waist of patient.
    :param height: Height of patient.
    :param expected: Expected body adiposity index.
    """
    assert get_body_adiposity_index(waist=waist, height=height) == expected


@pytest.mark.parametrize(
    'gender, waist, tg, hdl, bmi, expected',
    [
        # Males
        ('M', 111, 142, 32, 34.7, 2.9),
        ('M', 101, 110, 32, 30.7, 2.62),
        ('M', 99, 129, 38, 30.0, 2.57),
        ('M', 101, 109, 35, 31.5, 2.61),

        # Females
        ('F', 111, 142, 32, 34.7, 3.19),
        ('F', 101, 110, 32, 30.7, 2.87),
        ('F', 99, 129, 38, 30.0, 2.81),
        ('F', 101, 109, 35, 31.5, 2.86),

        # Fails
        ('O', 101, 142, 32, 34.7, ValueError)
    ]
)
def test_get_visceral_adiposity_index(gender: str, waist: int, tg: int, hdl: int, bmi: float,
                                      expected: Union[float, ValueError]):
    """
    Test the get visceral adiposity index formula.
    :param gender: Gender of patient.
    :param waist: Waist value.
    :param tg: Triglyceride value.
    :param hdl: HDL value.
    :param bmi: BMI of patient.
    :param expected: Expected visceral adiposity index formula.
    """
    if expected == ValueError:
        with pytest.raises(ValueError, match=GENDER_ERROR_MESSAGE):
            get_visceral_adiposity_index(gender=gender, waist=waist, tg=tg, hdl=hdl, bmi=bmi)
    else:
        assert get_visceral_adiposity_index(gender=gender, waist=waist, tg=tg, hdl=hdl, bmi=bmi) == expected


@pytest.mark.parametrize(
    'gender, waist, tg, expected',
    [
        # Males
        ('M', 111, 142, 73.75),
        ('M', 101, 110, 44.71),
        ('M', 99, 129, 49.52),
        ('M', 101, 109, 44.30),

        # Females
        ('F', 111, 142, 84.97),
        ('F', 101, 110, 53.4),
        ('F', 99, 129, 59.72),
        ('F', 101, 109, 52.92),

        # Fails
        ('O', 101, 142, ValueError)
    ]
)
def test_get_lipid_accumulation_product(gender: str, waist: int, tg: int, expected: Union[ValueError, float]):
    """
    Test the get lipid accumulation production function.
    :param gender: Gender of patient.
    :param waist: Waist of patient.
    :param tg: Triglyceride value.
    :param expected: Expected lipid accumulation product value.
    """
    if expected == ValueError:
        with pytest.raises(ValueError, match=GENDER_ERROR_MESSAGE):
            get_lipid_accumulation_product(gender=gender, waist=waist, tg=tg)
    else:
        assert get_lipid_accumulation_product(gender=gender, waist=waist, tg=tg) == expected


@pytest.mark.parametrize(
    'tg, ggt, waist, bmi, expected',
    [
        (142, 63, 111, 34.7, 93),
        (110, 41, 101, 30.7, 74),
        (129, 18, 99, 30.0, 59),
        (109, 55, 101, 31.5, 79)
    ]
)
def test_get_fatty_liver_index(tg: int, ggt: int, waist: int, bmi: float, expected: int):
    """
    Test the get fatty liver index retrieval function.
    :param tg: TG value.
    :param ggt: GGT value.
    :param waist: Waist value.
    :param bmi: BMI of patient.
    :param expected: Expected FLI.
    """
    assert get_fatty_liver_index(tg=tg, ggt=ggt, waist=waist, bmi=bmi) == expected


@pytest.mark.parametrize(
    'waist, height, expected',
    [
        (111, 166, 0.67),
        (101, 166, 0.61),
        (99, 166, 0.60),
        (101, 166, 0.61)
    ]
)
def test_get_waist_height_ratio(waist: int, height: int, expected: float):
    """
    Test get waist height ratio.
    :param waist: Waist of patient.
    :param height: Height of patient.
    :param expected: Expected waist/height ratio.
    """
    assert get_waist_height_ratio(waist=waist, height=height) == expected


@pytest.mark.parametrize(
    'alt, ast, expected',
    [
        (142, 77, 1.84),
        (50, 41, 1.22),
        (26, 27, 0.96),
        (38, 19, 2.0)
    ]
)
def test_get_alt_ast_ratio(alt: int, ast: int, expected: float):
    """
    Test get ALT/AST ratio.
    :param alt: ALT.
    :param ast: AST.
    :param expected: Expected ratio.
    """
    assert get_alt_ast_ratio(alt=alt, ast=ast) == expected


@pytest.mark.parametrize(
    'creatinine, gender, age, expected',
    [
        # Males
        (0.8, 'M', 65, 94),
        (0.9, 'M', 65, 90),
        (0.9, 'M', 65, 90),
        (0.7, 'M', 65, 99),

        # Females
        (0.8, 'F', 65, 78),
        (0.9, 'F', 65, 67),
        (0.9, 'F', 65, 67),
        (0.7, 'F', 65, 91),

        # Fails
        (0.8, 'O', 65, ValueError)
    ]
)
def test_get_egfr(creatinine: float, gender: str, age: int, expected: Union[ValueError, int]):
    """
    Test the get EGFR function.
    :param creatinine: Creatinine of patient.
    :param gender: Gender of patient.
    :param age: Age of patient.
    :param expected: Expected EGFR.
    """
    if expected == ValueError:
        with pytest.raises(ValueError, match=GENDER_ERROR_MESSAGE):
            get_egfr(creatinine=creatinine, gender=gender, age=age)
    else:
        assert get_egfr(creatinine=creatinine, gender=gender, age=age) == expected


@pytest.mark.parametrize(
    'hba1c, expected',
    [
        (7.2, 159.94),
        (5.6, 114.02),
        (5.9, 122.63),
        (7.5, 168.55),
    ]
)
def test_get_estimated_average_glucose(hba1c: float, expected: float):
    """
    Test the get estimated average glucose function.
    :param hba1c: Hba1c value.
    :param expected: Expected estimated average glucose.
    """
    assert get_estimated_average_glucose(hba1c=hba1c) == expected
