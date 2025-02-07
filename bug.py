def function_with_uncommon_error(a, b):
    if a == 0:
        return b / a  # ZeroDivisionError will occur only if a is exactly 0
    return a + b