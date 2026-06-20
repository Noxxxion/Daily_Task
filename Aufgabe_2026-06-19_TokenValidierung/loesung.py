def is_valid_token(token):
    """
    Validiert einen Token im Format XYZ-123-ABC.

    Args:
        token (str): Der zu validierende Token

    Returns:
        bool: True wenn der Token gültig ist, sonst False
    """
    if token is None:
        return False
    if not isinstance(token, str):
        return False
    if len(token) != 11:
        return False
    if token[3] != "-" or token[7] != "-":
        return False
    part1, part2, part3 = token.split("-")
    if not (part1.isalpha() and part1.isupper()):
        return False
    if not part2.isdigit():
        return False
    if not (part3.isalpha() and part3.isupper()):
        return False
    return True
