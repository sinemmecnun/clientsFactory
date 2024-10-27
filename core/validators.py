def validate_name(name):
    for s in name:
        if s.isdigit():
            return False
    return True


def validate_age(age):
    if int(age) >= 18:
        return True
    return False


def validate_egn(egn):
    if len(egn) == 10 and egn.isdigit():
        return True
    return False


def validate_iban(iban):
    if 34 < len(iban) < 20:
        return False
    if not iban[0:2].isalpha():
        return False
    return True


def validate_phone_number(phone_number):
    if not len(phone_number) == 10 or not phone_number.isdigit():
        return False

    phone_operators = ['089', '087', '088', '098']

    if not phone_number[0:3] in phone_operators:
        return False

    return True
