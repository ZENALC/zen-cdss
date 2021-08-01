"""
Basic formula functions for getting vitals.
"""
import math

GENDER_ERROR_MESSAGE = "Unknown type of gender provided. Valid genders are M and F for male and female respectively."


def get_homa_ir(insulin: float, glucose: float, round_digits: int = 2) -> float:
    """
    Returns the HOMA-IR (Insulin Resistance) based on insulin and glucose values provided.
    :param round_digits: Amount of digits to found by, by default, it'll be 2.
    :param insulin: Float value representing the insulin (µIU/mL) of patient.
    :param glucose: Float value representing the glucose (mg/dl) of patient.
    :return: HOMA-IR (Insulin Resistance) of patient.

    Parameters from Excel:
        C16 = insulin
        C17 = glucose

    Formula from Excel:
        =C16*C17/405
    """
    return round(insulin * glucose / 405, round_digits)


def get_bmi(weight: float, height: float, round_digits: int = 1) -> float:
    """
    Returns float value representing the body-mass-index of a patient in kg/sqm.
    :param round_digits: Amount of digits to found by, by default, it'll be 2.
    :param weight: Float value representing the weight of the patient in kilograms.
    :param height: Float value representing the height of the patient in centimeters.
    :return: Float value representing BMI.

    Parameters from Excel:
        C10 = weight
        C9 = height

    Formula from Excel:
        =C10/C9/C9*10000
    """
    return round(weight / height / height * 10_000, round_digits)


def get_blood_pressure(systolic_bp: int, diastolic_bp: int):
    """
    Returns the blood pressure of a patient based on systolic and diastolic blood pressures provided.
    :param systolic_bp: Systolic blood pressure of patient.
    :param diastolic_bp: Diastolic blood pressure of patient.
    :return: Blood pressure of the patient in a grade format. Available grades are: 3, 2, 1, low, ideal, and normal.

    Parameters from Excel:
        C13 = Systolic BP
        C14 = Diastolic BP

    Formula from Excel:
        =IF(OR(C13>=180,C14>=110),
            then "Grade 3",
            else:
                IF(OR(C13>=160,C14>=100),
                    then "Grade 2",
                    else IF(OR(C13>140,C14>90),
                        then "Grade 1",
                        else IF(OR(C13<90,C14<60),
                            then "Low",
                            IF(OR(AND(C13>89,C13<121,C14>59,C14<81)),
                                then "Ideal",
                                else "Normal")))))
    """
    if systolic_bp >= 180 or diastolic_bp >= 110:
        return 'Grade 3'
    elif systolic_bp >= 160 or diastolic_bp >= 100:
        return 'Grade 2'
    elif systolic_bp >= 140 or diastolic_bp >= 90:
        return 'Grade 1'
    elif systolic_bp < 90 or diastolic_bp < 60:
        return 'Low'
    elif 89 < systolic_bp < 121 and 59 < diastolic_bp < 81:
        return 'Ideal'
    else:
        return 'Normal'


def get_maximum_heart_rate(age: int) -> int:
    """
    Returns the maximum heart rate during exercise.
    :param age: Age of the patient.
    :return: Maximum heart rate appropriate for age provided.
    """
    return 220 - age


def get_target_heart_rate(maximum_heart_rate: int) -> str:
    """
    Returns the target heart rate based on maximum heart rate provided.
    :param maximum_heart_rate: Maximum heart rate during exercise of a patient.
    :return: Target heart rate based on the maximum heart rate provided.

    Parameter from Excel:
        K11 = Maximum heart rate.

    Formula from Excel:
        =(K11*0.5)&"-"&TRUNC(K11*0.85)
    """
    return f'{maximum_heart_rate * 0.5} - {math.floor(maximum_heart_rate * 0.85)}'


def get_tg_hdl_ratio(tg: int, hdl: int, round_digits: int = 2) -> float:
    """
    Returns float value of the TG/HDL ratio.
    :param tg: TG (mg/dL) of the patient.
    :param hdl: HDL (mg/dL) of the patient.
    :param round_digits: Amount of digits to found by, by default, it'll be 2.
    :return: Ratio of the TG / HDL ratio.
    """
    return round(tg / hdl, round_digits)


def get_triglyceride_glucose_index(tg: float, glucose: float, round_digits: int = 2) -> float:
    """
    Returns the triglyceride glucose index (TyG) based on the TG and glucose values provided.
    :param tg: TG (mg/dL) of the patient.
    :param glucose: Glucose (mg/dl) of the patient.
    :param round_digits: Amount of digits to found by, by default, it'll be 2.
    :return: Float value representing the triglyceride glucose index (TyG).

    Parameter from Excel:
        C19 = TG (mg/dL)
        C17 = Glucose (mg/dL)

    Formula from Excel:
        =LN(C19*C17)/2
    """
    return round(math.log(tg * glucose) / 2, round_digits)


def get_atherogenic_index_of_plasma(tg: float, hdl: float, round_digits: int = 2) -> float:
    """
    Returns the patient's atherogenic index of plasma.
    :param tg: TG (mg/dL) of the patient.
    :param hdl: HDL (mg/dL) of the patient.
    :param round_digits: Amount of digits to found by, by default, it'll be 0.
    :return: Float value representing the atherogenic index of plasma.

    Parameters from Excel:
        C19 = TG (mg/dL) of the patient.
        C20 = HDL (mg/dL) of the patient.

    Formula from Excel:
        =LOG10((C19/88.57)/(C20/38.67))
    """
    return round(math.log10((tg / 88.57) / (hdl / 38.67)), round_digits)


def get_body_adiposity_index(waist: float, height: float, round_digits: int = 0) -> float:
    """
    Returns the body adiposity index based on the waist and height provided.
    :param height: Height (cm) as a float.
    :param waist: Waist (cm) as a float.
    :param round_digits: Amount of digits to found by, by default, it'll be 0.
    :return: Float value representing the body adiposity index.

    Parameters from Excel:
        C12 = Waist
        C9 = Height

    Formula from Excel:
        =C12/POWER((C9/100),1.5)-18
    """
    return round(waist / (height / 100) ** 1.5 - 18, round_digits)


def get_visceral_adiposity_index(gender: str, waist: float, tg: int, hdl: int, bmi: float,
                                 round_digits: int = 2) -> float:
    """
    Returns the visceral adiposity index based on the gender, waist, TG, HDL, and BMI values provided.
    :param gender: Gender of the patient.
    :param waist: Waist of the patient in centimeters.
    :param tg: TG (mg/dL) of the patient.
    :param hdl: HDL (mg/dL) of the patient.
    :param bmi: BMI (kg/sqm) of the patient.
    :param round_digits: Amount of digits to found by, by default, it'll be 2.
    :return: Visceral adiposity index in a float format.

    Parameters from Excel:
        C11 = gender
        C12 = waist (cm)
        C19 = tg (mg/dL)
        C20 = HDL (mg/dL)
        K9 = BMI (kg/sqm)

    Formula from Excel:
        =IF(C11="M",(C12/39.68+(1.88*K9)*(C19/88.57/1.03)*(1.31/C20/38.67)),
        (C12/36.58+(1.89*K9) * (C19/88.57/0.81)*(1.52/C20/38.67)))
    """
    if gender == 'M':
        return round(waist / 39.68 + (1.88 * bmi) * (tg / 88.57 / 1.03) * (1.31 / hdl / 38.67), round_digits)
    elif gender == 'F':
        return round(waist / 36.58 + (1.89 * bmi) * (tg / 88.57 / 0.81) * (1.52 / hdl / 38.67), round_digits)
    else:
        raise ValueError(GENDER_ERROR_MESSAGE)


def get_lipid_accumulation_product(gender: str, waist: float, tg: float, round_digits: int = 2) -> float:
    """
    Returns the lipid accumulation product (LAP) based on the gender, waist, and TG (mg/dL) provided.
    :param gender: Gender of the patient.
    :param waist: Waist (cm) of the patient.
    :param tg: TG (mg/dL) of the patient.
    :param round_digits: Amount of digits to found by, by default, it'll be 2.
    :return: Float value representing the lipid accumulation product.

    Parameters from Excel:
        C11 = gender
        C12 = waist (cm)
        C19 = tg (mg/dL)

    Formula from Excel:
        =IF(C11="M",(C12-65)*(C19/88.57),(C12-58)*(C19/88.57))
    """
    if gender == 'M':
        return round((waist - 65) * (tg / 88.57), round_digits)
    elif gender == 'F':
        return round((waist - 58) * (tg / 88.57), round_digits)
    else:
        raise ValueError(GENDER_ERROR_MESSAGE)


def get_fatty_liver_index(tg: float, ggt: float, waist: float, bmi: float, round_digits: int = 0) -> float:
    """
    Returns the Fatty Liver Index (FLI) of a patient based on the TG, GGT, waist, and BMI provided.
    :param tg: TG (mg/dL) of the patient.
    :param ggt: GGT (U/L) of the patient.
    :param waist: Waist of the patient in centimeters.
    :param bmi: BMI (kg/sqm) of the patient.
    :param round_digits: Amount of digits to found by, by default, it'll be 0.
    :return: Float value representing the fatty live index.

    Parameters from Excel:
        C19 = TG (mg/dL) of the patient.
        C26 = GGT (U/L) of the patient.
        C12 = Waist of the patient in centimeters.
        K9 = BMI (kg/sqm) of the patient.
        EXP = e raised to the power.

    Formula from Excel:
        =EXP(SUM((0.953*LN(C19))+(0.139*K9)+(0.718*LN(C26))+(0.053*C12)-15.745))
        / (1+EXP(SUM((0.953*LN(C19)) + (0.139*K9)+(0.718*LN(C26))+(0.053*C12)-15.745))) * 100
    """
    initial_calculation = math.e ** (0.953 * math.log(tg) + 0.139 * bmi + (0.718 * math.log(ggt)) +
                                     (0.053 * waist) - 15.745)
    second_calculation = 1 + math.e ** (0.953 * math.log(tg) + (0.139 * bmi) + (0.718 * math.log(ggt)) + (0.053 * waist)
                                        - 15.745)
    return round(initial_calculation / second_calculation * 100, round_digits)


def get_waist_height_ratio(waist: int, height: int, round_digits: int = 2) -> float:
    """
    Returns the waist height ratio based on the waist and height provided.
    :param waist: Waist of the patient.
    :param height: Height of the patient.
    :param round_digits: Amount of digits to found by, by default, it'll be 2.
    :return: Float representing the waist/height ratio.
    """
    return round(waist / height, round_digits)


def get_alt_ast_ratio(alt: int, ast: int, round_digits: int = 2) -> float:
    """
    Returns the ratio of ALT/AST.
    :param alt: ALT (SGPT) (U/L) of the patient.
    :param ast: AST (SGOT) (U/L) of the patient.
    :param round_digits: Amount of digits to found by, by default, it'll be 2.
    :return: Float value of ALT/AST ratio.
    """
    return round(alt / ast, round_digits)


def get_egfr(creatinine: float, gender, age: int, round_digits: int = 0) -> float:
    """
    Returns the eGFR (CKD-EPI) based on the creatinine, gender, and age values provided.
    :param creatinine: Creatinine (mg/dl) of the patient.
    :param gender: Gender of the patient.
    :param age: Age of the patient as an integer.
    :param round_digits: Amount of digits to found by, by default, it'll be 0.
    :return: Float value representing the eGFR (CKD-EPI).

    Parameters from Excel:
        D8 = age
        D22 = creatinine
        D11 = gender

    Formula from Excel:
        =141 * MIN(D22*88.42/IF(D11="M",80,62),1) ^ IF(D11="M",-0.411,-0.329) * (MAX(D22*88.42/IF(D11="M",80,62),1))
        ^ (-1.209)*0.993^D8*IF(D11="M",1,1.018)
    """
    if gender == 'M':
        egfr = 141 * min(creatinine * 88.42 / 80, 1) ** -.411 * max(creatinine * 88.42 / 80, 1) ** -1.209 * .993 ** age
    elif gender == 'F':
        egfr = 141 * min(creatinine * 88.42 / 62, 1) ** -.329 * max(creatinine * 88.42 / 62, 1) ** -1.209 * \
               .993 ** age * 1.018
    else:
        raise ValueError(GENDER_ERROR_MESSAGE)

    return round(egfr, round_digits)


def get_estimated_average_glucose(hba1c: float, round_digits: int = 2) -> float:
    """
    Returns the estimated average glucose based on HbA1c provided.
    :param hba1c: HbA1c percentage.
    :param round_digits: Amount of digits to found by, by default, it'll be 2.
    :return: Float value representing the estimated average glucose.

    Parameter from Excel:
        C25 = HbA1C %

    Formula from Excel:
        =28.7*C25-46.7
    """
    return round(28.7 * hba1c - 46.7, round_digits)
