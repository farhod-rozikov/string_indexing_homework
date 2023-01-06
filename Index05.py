def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    d_count = 0
    if s[0].isdigit():
        d_count += 1
    if s[1].isdigit():
        d_count += 1
    if s[2].isdigit():
        d_count += 1
    if s[3].isdigit():
        d_count += 1
    if s[4].isdigit():
        d_count += 1
    return d_count